import zipfile

def extract_archive(archivepath, dest_dir):
	with zipfile.ZipFile(archivepath, 'r') as archive:
		archive.extractall(dest_dir)