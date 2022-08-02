from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class AppearObject(QGraphicsObject):
	clicked = Signal(object)
	
	def __init__(self, text, font, parent=None):
		super().__init__(parent)
		
		self.font = self.set_font(font)
		self.content = text
		self.font_measure = QFontMetrics(self.font)
		self.show = True
		self.margins = QMargins(5, 5, 5, 5)
		self.show_border = False
		self.border_pen = QPen(Qt.blue, 3, Qt.DashLine)
		self.text_options = QTextOption()
		self.text_options.setAlignment(Qt.AlignCenter)
		
	def boundingRect(self):
		c = self.mapToParent(0, 0)
		if self.show:
			return QRect(c.x(), c.y(), self.font_measure.width(self.content, Qt.AlignCenter)+self.margins.left()+self.margins.right(), self.font_measure.height()+self.margins.top()+self.margins.bottom())
		else:
			return QRect(c.x(), c.y(), 0, 0)
	
	def paint(self, painter, option, widget):
		painter.save()
		if self.show:
			painter.setFont(self.font)
			painter.drawText(self.boundingRect(), self.content, self.text_options)
		if self.show_border:
			painter.setPen(self.border_pen)
			painter.drawRect(self.boundingRect())
		painter.restore()
	
	def toggle_visibility(self):
		if self.show:
			self.show = False
		else:
			self.show = True
		return self
			
	def set_text(self, string):
		self.content = str(string)
		
	def set_font(self, font):
		if type(font) == QFont:
			return font
		elif type(font) == tuple:
			return QFont(font)
		else:
			return self.parent().font()
			
	def mousePressEvent(self, event):
		self.clicked.emit(self)
		super().mousePressEvent(event)
		
