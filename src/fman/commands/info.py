"""
info.py
Commands for displaying information about files and directories.

"""


from pathlib import Path
import os
from datetime import datetime


def path_info(path: str) -> dict:
    """
    Get information about a given path (file or directory).
    
    Args:
        path: String path to the file or directory
        
    Returns:
        Dictionary containing path information with keys:
            - name: Base name of the path
            - type: 'file', 'directory', 'symlink', or 'unknown'
            - absolute_path: Absolute path
            - exists: Whether the path exists
            - size: Size in bytes (None for directories)
            - is_symlink: Whether it's a symbolic link
            - permissions: File permissions in octal format
            - created: Creation time (ISO format)
            - modified: Last modification time (ISO format)
            - accessed: Last access time (ISO format)
            - is_hidden: Whether the file/directory is hidden (Windows)
    """
    p = Path(path).resolve()
    info_dict = {
        'name': p.name,
        'absolute_path': str(p.absolute()),
        'exists': p.exists(),
    }
    
    if not p.exists():
        info_dict['type'] = 'unknown'
        return info_dict
    
    # Determine type
    if p.is_symlink():
        info_dict['type'] = 'symlink'
    elif p.is_dir():
        info_dict['type'] = 'directory'
    elif p.is_file():
        info_dict['type'] = 'file'
    else:
        info_dict['type'] = 'unknown'
    
    # Get size
    if p.is_file():
        info_dict['size'] = p.stat().st_size
    else:
        info_dict['size'] = None
    
    # Get symlink info
    info_dict['is_symlink'] = p.is_symlink()
    
    # Get permissions
    stat_info = p.stat()
    info_dict['permissions'] = oct(stat_info.st_mode)[-3:]
    
    # Get timestamps
    info_dict['created'] = datetime.fromtimestamp(stat_info.st_ctime).isoformat()
    info_dict['modified'] = datetime.fromtimestamp(stat_info.st_mtime).isoformat()
    info_dict['accessed'] = datetime.fromtimestamp(stat_info.st_atime).isoformat()
    
    # Check if hidden (Windows/Unix)
    if os.name == 'nt':  # Windows
        info_dict['is_hidden'] = os.path.isfile(path) and os.stat(path).st_file_attributes & 0x02
    else:  # Unix-like
        info_dict['is_hidden'] = p.name.startswith('.')
    
    return info_dict
