import colorama

#speichert informationen von der Textur
class Texture:
	texture = "";
	fore_color = "";
	bg_color = "";
	style = "";
	visible = True;
	transparent = True;
	frames = [];
	
	#contructor von textur übergibt colorama hintergrundfarbe vordergrundfarbe style sowie transparents visibilität
	def __init__(self, texture, **kwargs):
		self.frames = [];
		self.texture = texture;
		self.fore_color = kwargs.get("fore_color",colorama.Fore.WHITE);
		self.style = kwargs.get("style",colorama.Style.NORMAL);
		self.bg_color = kwargs.get("bg_color",colorama.Back.BLACK);
		self.visible = kwargs.get("visible",True);
		self.transparent = kwargs.get("transparent",True);
		self.frames.append([0,0,texture,self.fore_color,self.style,self.bg_color,self.transparent])
	
	#fügt ein neues animations frame der textur hinzu
	def add_Frame(self,frame,state,texture, **kwargs):
		self.frames.append([frame,state,texture,kwargs.get("fore_color",colorama.Fore.WHITE),kwargs.get("style",colorama.Style.NORMAL),kwargs.get("bg_color",colorama.Back.BLACK),kwargs.get("transparent",True)]);
	
	#schaut welche textur relevant ist im spiel momentan
	def update(self,frame_index, state):
		for i in self.frames:
			if(i[0] == frame_index and i[1] == state):
				self.texture = i[2];
				self.fore_color = i[3];
				self.style = i[4];
				self.bg_color = i[5];
				self.transparent = i[6];