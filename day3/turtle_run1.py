import turtle as t

wn = t.Screen()
wn.bgcolor("lightgreen") # Set the window background color
wn.title("Turtle Run Ver.1")

move = 20

def turn_right():
    t.setheading(0) #거북이의 머리 방향을 0도로 돌린다.
    t.forward(move)

def turn_left():
    t.setheading(180) #거북이의 머리 방향을 180도 돌린다
    t.forward(move)

def turn_up():
    t.setheading(90)
    t.forward(move)

def turn_down():
    t.setheading(270)
    t.forward(move)

def reset():
    t.clear()  #화면을 리셋

t.shape("turtle")
t.speed(0)
t.penup()
t.color("black","lightgreen")
t.onkeypress(turn_right, "Right") # 오른쪽 방향키가 눌리면 turn_right 함수 수행
t.onkeypress(turn_left, "Left")   # 왼쪽  방향키가 눌리면 turn_left 함수 수행
t.onkeypress(turn_up, "Up")       # 위쪽 방향키가 눌리면 turn_up 함수 수행
t.onkeypress(turn_down, "Down")   # 아래쪽 방향키가 눌리면 turn_down 함수 수행
t.onkeypress(reset, "r") #r키가 눌리면 reset 함수 수행
t.listen() #입력을 기다림...

             
