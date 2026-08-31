from pathlib import Path
from typing import List


def find_path(
        start_path: str,
        name_pattern: str,
        search_type: str = 'both',
        recursive: bool = True
    ) -> List[dict]:
        """
        Find files or directories matching a given name pattern.
        
        Args:
            start_path: Starting directory path to search from
            name_pattern: Name or pattern to search for (supports wildcards like *)
            search_type: Type of items to search for - 'file', 'dir', or 'both' (default: 'both')
            recursive: Whether to search recursively in subdirectories (default: True)
            
        Returns:
            List of dictionaries containing matched items with keys:
                - name: Name of the file/directory
                - path: Full absolute path
                - type: 'file' or 'directory'
                - size: Size in bytes (for files)
                
        Raises:
            FileNotFoundError: If the start_path does not exist
            NotADirectoryError: If the start_path is not a directory
            ValueError: If search_type is invalid
        """
        # Validate inputs
        if search_type not in ('file', 'dir', 'both'):
            raise ValueError("search_type must be 'file', 'dir', or 'both'")
        
        start = Path(start_path).resolve()
        
        if not start.exists():
            raise FileNotFoundError(f"Path {start_path} does not exist.")
        
        if not start.is_dir():
            raise NotADirectoryError(f"Path {start_path} is not a directory.")
        
        matches = []
        
        # Determine search method
        if recursive:
            search_iter = start.rglob(name_pattern)
        else:
            search_iter = start.glob(name_pattern)
        
        for item in search_iter:
            # Filter by type
            if search_type == 'file' and not item.is_file():
                continue
            elif search_type == 'dir' and not item.is_dir():
                continue
            
            # Gather information
            item_info = {
                'name': item.name,
                'path': str(item.absolute()),
                'type': 'directory' if item.is_dir() else 'file'
            }
            
            # Add size for files
            if item.is_file():
                try:
                    item_info['size'] = item.stat().st_size
                except (OSError, PermissionError):
                    item_info['size'] = None
            else:
                item_info['size'] = None
            
            matches.append(item_info)
        
        # Sort by path
        return sorted(matches, key=lambda x: x['path'])
