import turtle

window = turtle.Screen()
window.bgcolor("white")
supert = turtle.Turtle()
supert.shape("turtle")

def superturtle_draw(xmove, ymove):
	def draw():
		countturns = 0
		for i in range(1):
			make_moon()
			countturns += 1
			if countturns > 0:
				make_flag()

	def make_pole():
		supert.left(ymove)
		supert.forward((xmove))
		supert.right(ymove)

	def make_triangle():
		supert.right(ymove/2)
		supert.forward((xmove/2))
		supert.right(ymove*1.5)
		supert.forward((xmove/3.5))

	def make_flag():
		make_pole()
		make_triangle()

	def make_moon():
		for i in range(8):
			supert.forward((xmove/4))
			supert.right((ymove/4))
			supert.forward((xmove/4))
			supert.right((ymove/4))
		

	return draw()

def main():
	superturtle_draw(100,90)

main()

window.exitonclick()