class Utilities:
    """Utility functions for text processing and data manipulation."""
    
    @staticmethod
    def remove_accents(text: str) -> str:
        """
        Remove accents and special characters from text for normalization.
        
        Args:
            text (str): The input text that may contain accented characters.
            
        Returns:
            str: The text with accents removed and normalized.
            
        Example:
            >>> Utilities.remove_accents("café")
            'cafe'
            >>> Utilities.remove_accents("España")
            'Espana'
        """
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
            'ü': 'u', 'Ü': 'U', 'ñ': 'n', 'Ñ': 'N'
        }
        for accented, unaccented in replacements.items():
            text = text.replace(accented, unaccented)
        return text