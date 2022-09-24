from fastapi import FastAPI,HTTPException,status,Request,Form
from Logistic_api import schema
from Logistic_api import model
from Logistic_api.database import engine, SessionLocal
from fastapi.params import Depends
from sqlalchemy.orm import  Session
import warnings
# from sklearn.linear_model import LogisticRegression
# import pandas as pd
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import joblib 
# file_csv=pd.read_csv("Logistic_api/Fish.csv")
# x=file_csv.iloc[:,1:].values
# y=file_csv.iloc[:,0:-6].values
app=FastAPI(
    title="Linear Discrimant Analysis ML API With Connection to Azure Mysql Database",
description="To determine Species of Fish given all the parameters"
)
model.Base.metadata.create_all(engine)
with warnings.catch_warnings():
      warnings.simplefilter("ignore", category=UserWarning)
      pipe_lr = joblib.load(open("Logistic_api/logistic_model/fishapipred (1).pkl","rb"))
def predict(docx):
    results = pipe_lr.predict(docx)
    return results[0]
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
clf = LogisticRegression()
clf.fit(x,y)
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
 
@app.get("/frontend", response_class=HTMLResponse)
async def read_item(request: Request):
    weight = ""
    length1=""
    length2=''
    length3=''
    height=''
    width=''
    species=''

    return templates.TemplateResponse("item.html",context={'request': request, 'weight': weight,'length1':length1,'length2':length2,'length3':length3,'height':height,'width':width,'species':species})
@app.post("/frontend")
def form_post(request: Request, Weight: float = Form(...),Length1:float=Form(...),Length2:float=Form(...),Length3:float=Form(...),Height:float=Form(...),Width:float=Form(...)):
    weight =Weight
    length1=Length1
    length2=Length2
    length3=Length3
    height=Height
    width=Width
    test_data = [[weight, length1, length2,length3, height, width]]
    class_idx =predict(test_data)
    #clf.predict(test_data)[0]
    species = class_idx


    return templates.TemplateResponse('item.html', context={'request': request, 'weight': weight,'length1':length1,'length2':length2,'length3':length3,'height':height,'width':width,'species':species})

@app.get('/')
def welcome():
    return {f'Home page of fastapi and i have connected with azure MySQL database '}


@app.get('/predictions')
def prediction_table(db:Session=Depends(get_db)):
    predicted=db.query(model.logistic_api).all()
    return predicted

@app.get('/predictions/{id}')
def prediction_table(id:int,db:Session=Depends(get_db)):
    predicted=db.query(model.logistic_api).filter(model.logistic_api.id==id).first()
    if not predicted:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id Not Found")
    return predicted

@app.delete('/predictions/{id}')
def delete(id:int,db:Session=Depends(get_db)):
    db.query(model.logistic_api).filter(model.logistic_api.id==id).delete(synchronize_session=False)
    db.commit()
    return {f'Prediction with id:{id} deleted succesfully'}

@app.put('/predictions/{id}')
def update(id:int,request:schema.logistic,db:Session=Depends(get_db)):
    update1=db.query(model.logistic_api).filter(model.logistic_api.id==id)
    if not update1.first():
        pass
    update1.update(request.dict())
    db.commit()
    return{f'succesfully updated id:{id}'}
@app.post('/predict',status_code=status.HTTP_201_CREATED)
async def add(request:schema.logistic,db:Session=Depends(get_db)):
    test_data=[[
        request.Weight,
        request.Length1,
        request.Length2,
        request.Length3,
        request.Height,
        request.Width
    ]]
    class_idx = predict(test_data)
    #clf.predict(test_data)[0]
    request.Species=class_idx
    new_logistic_api = model.logistic_api(Weight=request.Weight,Length1=request.Length1,Length2=request.Length2,Length3=request.Length3,Height=request.Height,Width=request.Width,Species=request.Species)
    db.add(new_logistic_api)
    db.commit()
    db.refresh(new_logistic_api)
    return request
