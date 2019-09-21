
#öffnet angegebene Datei und gibt die gewünschte textur zurück
def load_texture(file,texture):
	file = open("textures/"+file,"r",encoding="utf-8");
	return file.readlines()[texture].replace("\\n","\n");