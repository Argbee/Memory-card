#подключение всякого
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QButtonGroup, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox
from random import shuffle, randint


#Создание приложения и окна
app = QApplication([])
main_manu = QWidget()
main_manu.setWindowTitle('Memory Card')
main_manu.resize(500, 350)
quation = QLabel('')
oke_btn = QPushButton('Ответить')
#основные Линии в окне
vlayout = QVBoxLayout()
hlayout_1 = QHBoxLayout()
hlayout_2 = QHBoxLayout()
#class qua
    #Группа "Кнопки"
ans_1 = QRadioButton('')
ans_2 = QRadioButton('')
ans_3 = QRadioButton('')
ans_4 = QRadioButton('')


RadioGroup = QButtonGroup() 
RadioGroup.addButton(ans_1)
RadioGroup.addButton(ans_2)
RadioGroup.addButton(ans_3)
RadioGroup.addButton(ans_4)

#Группа "Вопросы" с их линиями
RadioGroupBox = QGroupBox('Варианты ответов:')
vglayout = QVBoxLayout()
hglayout_1 = QHBoxLayout()
hglayout_2 = QHBoxLayout()

hglayout_1.addWidget(ans_1)
hglayout_1.addWidget(ans_2)
hglayout_2.addWidget(ans_3)
hglayout_2.addWidget(ans_4)
vglayout.addLayout(hglayout_1)
vglayout.addLayout(hglayout_2)

RadioGroupBox.setLayout(vglayout)
hlayout_1.addWidget(quation, alignment = Qt.AlignCenter)


#Группа "Результаты" с их линиями

RightNotRGroup = QGroupBox('Результат теста')
result = QLabel('Правильно\Неправильно')
r_result = QLabel('')
nothing = QLabel('  ')#Ну прям реально nothing

vglayout_2 = QVBoxLayout()
hglayout_3 = QHBoxLayout()
hglayout_4 = QHBoxLayout()
hglayout_5 = QHBoxLayout()

hglayout_3.addWidget(result, alignment = Qt.AlignLeft)
hglayout_4.addWidget(r_result, alignment = Qt.AlignCenter)
hglayout_5.addWidget(nothing, alignment = Qt.AlignCenter)
vglayout_2.addLayout(hglayout_3)
vglayout_2.addLayout(hglayout_4)
vglayout_2.addLayout(hglayout_5)

RightNotRGroup.setLayout(vglayout_2)
#Линии в целом на окне
hlayout_2.addStretch(1)
hlayout_2.addWidget(oke_btn, stretch = 2)
hlayout_2.addStretch(1)
vlayout.addLayout(hlayout_1)
vlayout.addWidget(RightNotRGroup)
vlayout.addWidget(RadioGroupBox)
vlayout.addLayout(hlayout_2)
vlayout.setSpacing(30)

vglayout_2.setSpacing(30)

main_manu.setLayout(vlayout)   

class Question(object):
  def __init__(self, question, answer_right, wrong1, wrong2, wrong3):
    global ans_1, ans_2, ans_3, ans_4, RadioGroupBox, RadioGroup, result, r_result, RightNotRGroup
    self.question = question,
    self.answer_right = answer_right
    self.wrong1 = wrong1
    self.wrong2 = wrong2
    self.wrong3 = wrong3
    #Тестовое
    RadioGroupBox.show()
    RightNotRGroup.hide()
  #Вопрос показать
  def show_qua(self): 
    oke_btn.setText('Ответить') 
    RadioGroupBox.show()
    RightNotRGroup.hide()
    next_question()

Quation = 'Какой национальности не существует?'
q = Question("", "", "", "", "")
num_of_questions = [['Какого цвета нет на флаге России?', 'Зеленый', 'Синий', 'Белый', 'Красный'], ['Государственный язык Бразилии', 'Португальский', 'Бразильский', 'Испанский', 'Английский'], [' Выбери перевод слова "Переменная" ', ' variable ', ' variation ', ' changing ', ' variant '], ['Какой национальности не существует?', 'Энцы', 'Смурфы', 'Алеуты', 'Чулымцы']]
def next_question():
  global Quation, q

  random_number = (randint(0, len(num_of_questions) - 1))
  Another_que = num_of_questions[random_number]
  q = Question(Another_que[0], Another_que[1], Another_que[2], Another_que[3], Another_que[4])
  Quation = str(q.question)
  Quation = Quation.translate({ord(i):None for i in "'(),"})
  quation.setText(Quation)
  num_of_questions.remove(Another_que)
  answerss = [str(q.answer_right), str(q.wrong1), str(q.wrong2), str(q.wrong3)]
  shuffle(answerss)
  ans_1.setText(answerss[0])
  ans_2.setText(answerss[1])
  ans_3.setText(answerss[2])
  ans_4.setText(answerss[3])



#def ask(q: Question):
#  next_question()
#  answerss = [str(q.answer_right), str(q.wrong1), str(q.wrong2), str(q.wrong3)]
#  shuffle(answerss)
#  ans_1.setText(answerss[0])
#  ans_2.setText(answerss[1])
#  ans_3.setText(answerss[2])
#  ans_4.setText(answerss[3])
  





#Счетчик меняющий наполнение q и считающий кол-во вопросов. И счетчик правильных ответов
num_que = 0
count_r_ans = 0

#Доп функции
#Показать результат
def show_result():  
 oke_btn.setText('Следующий вопрос')
 RadioGroupBox.hide()
 RadioGroup.setExclusive(False)
 ans_1.setChecked(False)
 ans_2.setChecked(False)
 ans_3.setChecked(False)
 ans_4.setChecked(False)
 RadioGroup.setExclusive(True)
 r_result.setText(str(q.answer_right))

 RightNotRGroup.show()



#Какая кнопка
def check_btn():
 global num_que, q
 some_text = oke_btn.text()
 num_que = num_que + 0.5
 if some_text == 'Ответить':
   Check_answer(ans_1)
   Check_answer(ans_2)
   Check_answer(ans_3)
   Check_answer(ans_4)
   show_result()
 elif some_text == 'Следующий вопрос':
  q.show_qua()



def print_stat():
  print('Статистика\n-Всего вопросов:', int(num_que + 0.5), '\n-Правильных ответов:', count_r_ans, '\n-Рейтинг:', (count_r_ans / (num_que + 0.5) * 100))




#Проверить работает или нет
def Check_answer(ans):
  not_textovoe = ans
  textovoe = ans
  textovoe = textovoe.text()
  def chel():
    global count_r_ans
    if textovoe == q.answer_right:
      result.setText('Правильно!')
      count_r_ans = count_r_ans + 1
    if textovoe != q.answer_right:
      result.setText('Неправильно :(')   
    print_stat()
  not_textovoe.toggled.connect(chel)
  #oke_btn.clicked.connect(chel)



next_question()

oke_btn.clicked.connect(check_btn)

main_manu.show()
app.exec_()

