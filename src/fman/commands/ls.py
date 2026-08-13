from pathlib import Path


def list_dir(path: str) -> list:
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
    p = Path(path)
    
    if not p.exists():
        raise FileNotFoundError(f"Path {path} does not exist.")
    
    if not p.is_dir():
        raise NotADirectoryError(f"Path {path} is not a directory.")
    
    directories = []
    
    for entry in p.iterdir():
        if entry.is_dir():
            try:
                dir_size = sum(f.stat().st_size for f in entry.rglob('*') if f.is_file())
            except (OSError, PermissionError):
                dir_size = 0
            
            directories.append({
                'name': entry.name,
                'path': str(entry.absolute()),
                'size': dir_size
            })
    
    return sorted(directories, key=lambda x: x['name'])