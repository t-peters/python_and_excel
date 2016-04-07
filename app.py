from flask import Flask,render_template,request
import openpyxl


app = Flask('__main__')

def read_excel():
  wb = openpyxl.load_workbook("./test.xlsx")

  data = wb.get_sheet_by_name('Sheet1')
  return data

@app.route('/')
def index():
  
  return render_template('index.html',names=read_excel().columns[2])


@app.route('/get_student/<row>')

def get_student(row):
  club = [
      ['Art','5'],
      ['Catering and Craft','6'],
      ['Busy Hands','6'],
      ['Chess','5'],
      ['Choreography','8'],
      ['Drama','8'],
      ['Elocution and Debate','5'],
      ['Graphic Art and Animation','10'],
      ['Music/Band','5'],
      ['Press','5'],
      ['Photography','8'],
      ['Readers','5'],
      ['Science','6'],
      ['Young Farmers Club','5']
  ]

  extraco = [
      ['Fitness','15'],
      ['Double-dutch','15'],
      ['Football','15'],
      ['Martial Arts','15']
  ]
  return render_template('student.html',student=read_excel().rows[int(row)],clubs=club,extra=extraco)




if __name__ == '__main__':
  app.debug = True
  app.run()