# -*-coding:utf-8-*-
from flask import Flask,render_template,request,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import config,datetime

app = Flask(__name__)
app.config.from_object(config)
db =SQLAlchemy(app,use_native_unicode='utf8')


class ProjectInfo(db.Model):
    __tablename__ = 'projectinfo'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ProjectId = db.Column(db.String(100), nullable=False)
    Contract = db.Column(db.String(50), nullable=False)
    ProjectName = db.Column(db.String(100))
    Sale = db.Column(db.String(10))
    Customer = db.Column(db.String(50))
    Time = db.Column(db.DateTime)

    def __init__(self, ProjectId,Contract,ProjectName,Sale,Customer,Time):
        self.ProjectId = ProjectId
        self.Contract = Contract
        self.ProjectName = ProjectName
        self.Sale = Sale
        self.Customer = Customer
        self.Time = Time

    def __repr__(self):
        return '<ProjectId %r>' % self.ProjectId

db.create_all()


l = []
@app.route('/api',methods=['GET'])
def api():
    result = ProjectInfo.query.all()
    for i in result:
        data = dict(zip(('ProjectId','Contract','ProjectName','Sale','Customer','Time'),(i.ProjectId,i.Contract,i.ProjectName,i.Sale,i.Customer,i.Time)))
        l.append(data)
        print(data)
    return jsonify(l)





@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


@app.route('/pre_analysis', methods=['GET','POST'])
def pre_analysis():
    if request.method == 'POST':
        projectId = request.form.get('projectId')
        contractId = request.form.get('contractId')
        customerName = request.form.get('customerName')
        customerPhone = request.form.get('customerPhone')
        customerAddress = request.form.get('customerAddress')
        projectName = request.form.get('projectName')
        sales = request.form.get('sales')
        salesPhone = request.form.get('salesPhone')
        salesEmail = request.form.get('salesEmail')
        technicalSupport = request.form.get('technicalSupport')
        technicalPhone = request.form.get('technicalPhone')
        technicalEmail = request.form.get('technicalEmail')
        shiji = request.form.getlist('shiji')
        Samplelabel = request.form.get('Samplelabel')
        ProtExtract = request.form.get('ProtExtract')
        Enzymetext = request.form.get('Enzymetext')
        HPLC = request.form.get('HPLC')
        Modenrich = request.form.get('Modenrich')
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        project = ProjectInfo(projectId,contractId,projectName,sales,customerName,nowTime)
        db.session.add(project)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('pre_analysis.html')


@app.route('/stand_analysis')
def stand_analysis():
    return render_template('stand_analysis.html')

@app.route('/project_query')
def project_query():
    return render_template('project_query.html')

@app.route('/project_manage')
def project_manage():
    return render_template('project_manage.html')



if __name__ == '__main__':
    app.run(debug=True)
