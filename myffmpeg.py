import sys
import subprocess

argc = len( sys.argv )

for i in range( argc ):
	if i > 0:
		input_file = sys.argv[ i ]
		output_file = input_file[:-4] + '-24.mov'
		output = subprocess.run( 'which ffmpeg', shell = True, capture_output=True, text=True );
		ffmpeg_path = output.stdout.strip()

		command = ffmpeg_path + ' -i ' + "'" + input_file + "'" + ' -r 24 -vf scale=-1:720 ' + "'" + output_file + "'"

		print( command )

		subprocess.run( command, shell = True )
