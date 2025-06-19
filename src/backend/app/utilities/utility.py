class Utilities:
    @staticmethod
    def remove_accents(text: str) -> str:
        replacements = {
            'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
            'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
            'ü': 'u', 'Ü': 'U', 'ñ': 'n', 'Ñ': 'N'
        }
        for accented, unaccented in replacements.items():
            text = text.replace(accented, unaccented)
        return text