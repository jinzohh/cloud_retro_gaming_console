import boto3
from botocore.exceptions import ClientError
import logging
import time
import subprocess, sys, os

aws_access_key = 'XXXXXXXXXXXXXXX' # Your AWS access key
aws_secret_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' # Your AWS secret key

bucket = 'xxxxxxxx' # Your bucket name
prefix_snes = 'snes'
prefix_psx = 'psx'
prefix_nes = 'nes'

s3 = boto3.client(
     's3',
     aws_access_key_id=aws_access_key,
     aws_secret_access_key=aws_secret_key
)

def list_objects(bucket_name, prefix_name):
     """list all objects from an Amazon S3 bucket"""
     try:
          response = s3.list_objects(Bucket=bucket_name, Prefix=prefix_name)
     except ClientError as e:
          logging.error(e)
          return None
     return response

def list_snes():
     # List games for SNES
     files_snes = list_objects(bucket, prefix_snes)
     files_snes = files_snes.get("Contents")[1:]

     for file in files_snes:
          store_displayName = str(file['Key']).split('.',1)[0]
          #print(store_displayName)

          # Make sure to insert your Odroid username below
          with open('/home/<NameOfYourChoice>/RetroPie/roms/store/' + store_displayName + '.py', 'w') as f:
               f.write(
                    'import boto3\n'
                    'from botocore.exceptions import ClientError\n'
                    'import logging\n'
                    'import subprocess, sys, os\n'
                    'import time\n'
                    '\n'
                    'store_displayName = str(os.path.basename(__file__)).split(\'.\',1)[0]\n'
                    # Make sure to insert your Odroid username below
                    'outputName = \'/home/<NameOfYourChoice>/RetroPie/roms/snes/\' + store_displayName + \'.zip\'\n'
                    'aws_access_key = \'XXXXXXXXXXXXXXX\'\n' # Your AWS access key
                    'aws_secret_key = \'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\'\n' # Your AWS secret key
                    'bucket = \'xxxxxxxx\'\n' # Your bucket name
                    'key = \'snes/\' + store_displayName + \'.zip\'\n'
                    's3 = boto3.client(\'s3\', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)\n'
                    's3.download_file(bucket, key, outputName)\n'
                    'print("Success! Game saved in Super Nintendo.")\n'
                    'proc = subprocess.Popen([\'killall\', \'emulationstation\'], shell=False)\n'
                    'print("Restarting Emulationstation...")\n'
                    'time.sleep(2)\n'
                    'proc = subprocess.Popen([\'emulationstation\'], shell=False)\n'
               )
          # Make sure to insert your Odroid username below
          args = ['chmod', '+x', ('/home/<NameOfYourChoice>/RetroPie/roms/store/' + store_displayName + '.py')]
          proc = subprocess.Popen(args, shell=False)

def list_psx():
     # List games for PSX
     files_psx = list_objects(bucket, prefix_psx)
     files_psx = files_psx.get("Contents")[1:]

     for file in files_psx:
          store_displayName = str(file['Key']).split('.',1)[0]
          #print(store_displayName)

          # Make sure to insert your Odroid username below
          with open('/home/<NameOfYourChoice>/RetroPie/roms/store/' + store_displayName + '.py', 'w') as f:
               f.write(
                    'import boto3\n'
                    'from botocore.exceptions import ClientError\n'
                    'import logging\n'
                    'import subprocess, sys, os\n'
                    'import time\n'
                    '\n'
                    'store_displayName = str(os.path.basename(__file__)).split(\'.\',1)[0]\n'
                    # Make sure to insert your Odroid username below
                    'outputName = \'/home/<NameOfYourChoice>/RetroPie/roms/psx/\' + store_displayName + \'.7z\'\n'
                    'aws_access_key = \'XXXXXXXXXXXXXXX\'\n' # Your AWS access key
                    'aws_secret_key = \'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\'\n' # Your AWS secret key
                    'bucket = \'xxxxxxxx\'\n' # Your bucket name
                    'key = \'psx/\' + store_displayName + \'.7z\'\n'
                    's3 = boto3.client(\'s3\', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)\n'
                    's3.download_file(bucket, key, outputName)\n'
                    'print("Success! Game saved in Playstation.")\n'
                    'proc = subprocess.Popen([\'killall\', \'emulationstation\'], shell=False)\n'
                    'print("Restarting Emulationstation...")\n'
                    'time.sleep(2)\n'
                    'proc = subprocess.Popen([\'emulationstation\'], shell=False)\n'
               )
          # Make sure to insert your Odroid username below
          args = ['chmod', '+x', ('/home/<NameOfYourChoice>/RetroPie/roms/store/' + store_displayName + '.py')]
          proc = subprocess.Popen(args, shell=False)

def list_nes():
     # List games for NES
     files_nes = list_objects(bucket, prefix_nes)
     files_nes = files_nes.get("Contents")[1:]

     for file in files_nes:
          store_displayName = str(file['Key']).split('.',1)[0]
          #print(store_displayName)

          # Make sure to insert your Odroid username below
          with open('/home/<NameOfYourChoice>/RetroPie/roms/store/' + store_displayName + '.py', 'w') as f:
               f.write(
                    'import boto3\n'
                    'from botocore.exceptions import ClientError\n'
                    'import logging\n'
                    'import subprocess, sys, os\n'
                    'import time\n'
                    '\n'
                    'store_displayName = str(os.path.basename(__file__)).split(\'.\',1)[0]\n'
                    # Make sure to insert your Odroid username below
                    'outputName = \'/home/<NameOfYourChoice>/RetroPie/roms/nes/\' + store_displayName + \'.zip\'\n'
                    'aws_access_key = \'XXXXXXXXXXXXXXX\'\n' # Your AWS access key
                    'aws_secret_key = \'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\'\n' # Your AWS secret key
                    'bucket = \'xxxxxxxx\'\n' # Your bucket name
                    'key = \'nes/\' + store_displayName + \'.zip\'\n'
                    's3 = boto3.client(\'s3\', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)\n'
                    's3.download_file(bucket, key, outputName)\n'
                    'print("Success! Game saved in Playstation.")\n'
                    'proc = subprocess.Popen([\'killall\', \'emulationstation\'], shell=False)\n'
                    'print("Restarting Emulationstation...")\n'
                    'time.sleep(2)\n'
                    'proc = subprocess.Popen([\'emulationstation\'], shell=False)\n'
               )
          # Make sure to insert your Odroid username below
          args = ['chmod', '+x', ('/home/<NameOfYourChoice>/RetroPie/roms/store/' + store_displayName + '.py')]
          proc = subprocess.Popen(args, shell=False)

while True:
     list_snes()
     list_psx()
     list_nes()
     time.sleep(10) # Update from AWS cloud every 10 seconds
