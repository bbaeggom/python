import turtle as t

a = t.Turtle()
b = t.Turtle()
c = t.Turtle()

a.shape("turtle") #주인공
b.shape("turtle") #악당
c.shape("circle") #먹이

a.color("blue")  #주인공 파란색
b.color("red")   #악당 빨간색
c.color("green") #먹이 초록색

a.speed(20)
b.speed(10)
c.speed(0)

b.up()
b.goto(0, 200) #위 방향으로 200 이동

c.up()
c.goto(0, -200) #아래 방향으로 200 이동
