import sys
import subprocess

argc = len( sys.argv )

for i in range( argc ):
	if i > 0:
		input_file = sys.argv[ i ]
		output_file = input_file[:-4] + '-24.mov'
		command = '/opt/homebrew/Cellar/ffmpeg/4.4_2/bin/ffmpeg -i ' + "'" + input_file + "'" + ' -r 24 -vf scale=-1:720 ' + "'" + output_file + "'"

		print( command )

		subprocess.run( command, shell = True )
