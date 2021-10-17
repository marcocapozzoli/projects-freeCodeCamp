class Rectangle:

	def __init__(self, width, height):
		self._width = width
		self._height = height

	def set_width(self, width):
		self._width = width

	def set_height(self, height):
		self._height = height

	def get_area(self):
		return self._width * self._height

	def get_perimeter(self):
		return 2 * self._width + 2 * self._height

	def get_diagonal(self):
		return (self._width ** 2 + self._height ** 2) ** .5		

	def get_picture(self):
		
		if self._height > 50 or self._width > 50:
			return "Too big for picture."
		else:		
  		    for i in range(self._height):
        		return f"{'*' * self._width}\n" * self._height
  

	def get_amount_inside(self):
		pass

rect = Rectangle(6,6)
print(rect.get_picture())


class Square(Rectangle):
  pass
