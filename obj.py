import colorama
from vector2d import Vector2D
from texture import Texture

#leere hintergrund textur object klasse
class Obj:
	pos = Vector2D(0,0);
	texture = None;
	
	#erstellt Objekt nach übergebener position texture sowie weiteren optionalen attributen
	def __init__(self,pos,texture, **kwargs):
		self.pos = pos;
		transparent = kwargs.get("transparent",True);
		fore_color = kwargs.get("fore_color",colorama.Fore.WHITE)
		style = kwargs.get("style",colorama.Style.NORMAL)
		bg_color = kwargs.get("bg_color",colorama.Back.BLACK)
		self.texture = Texture(texture,fore_color = fore_color,bg_color = bg_color,style = style,transparent = transparent);