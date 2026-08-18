from pathlib import Path


def list_dir(path: str = ".") -> list:
    """
    Get a list of directories in the given path.
    
    Args:
        path: String path to the directory
        
    Returns:
        List of dictionaries containing directory information:
            - name: Name of the directory
            - path: Full path to the directory
            - size: Total size of the directory
            
    Raises:
        FileNotFoundError: If the path does not exist
        NotADirectoryError: If the path is not a directory
    """
    p = Path(path).resolve()
    
    if not p.exists():
        raise FileNotFoundError(f"Path {path} does not exist.")
    
    if not p.is_dir():
        raise NotADirectoryError(f"Path {path} is not a directory.")
    
    
    
    items = []
    
    for entry in p.iterdir():
        # 1. Eğer bir klasörse (Directory)
        if entry.is_dir():
            try:
                # Klasörün içindeki tüm dosyaların boyutunu topla
                dir_size = sum(f.stat().st_size for f in entry.rglob('*') if f.is_file())
            except (OSError, PermissionError):
                dir_size = 0
            
            items.append({
                'name': entry.name,
                'path': str(entry.absolute()),
                'size': dir_size,
                'type': 'Dir'  # Tipini belirtelim ki cli.py kolayca ayırt etsin
            })
            
        # 2. Eğer bir dosyaysa (File)
        elif entry.is_file():
            try:
                file_size = entry.stat().st_size  # Direkt dosyanın kendi boyutunu al
            except (OSError, PermissionError):
                file_size = 0
                
            items.append({
                'name': entry.name,
                'path': str(entry.absolute()),
                'size': file_size,
                'type': 'File'  # Tipini belirtelim
            })
    
    # İsme göre sıralayıp döndür
    return sorted(items, key=lambda x: x['name'])
