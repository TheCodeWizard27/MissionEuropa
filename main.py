import colorama
import os

from engine import Engine

#haupt Funktion wodurch das Spiel gestartet wird
def main():
	colorama.init();
	os.system("mode con: cols=150 lines=51");
	engine = Engine();
	
main();