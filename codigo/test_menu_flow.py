import sys
import os
import unittest
from unittest.mock import patch
from io import StringIO

# Add the code directory to path
sys.path.append(os.path.join(os.getcwd(), 'codigo'))

from main import menuPersonalizado

class TestMenuFlow(unittest.TestCase):
    
    @patch('builtins.input')
    @patch('sys.stdout', new_callable=StringIO)
    def test_default_matrix_coo_flow(self, mock_stdout, mock_input):
        # Inputs:
        # 1: Usar matriz predeterminada
        # 1: COO
        # 2: Obtener elemento
        # 0: Fila 0
        # 1: Columna 1
        # 8: Salir
        # Enter: Volver al menu principal
        mock_input.side_effect = ['1', '1', '2', '0', '1', '8', '']
        
        menuPersonalizado()
        
        output = mock_stdout.getvalue()
        self.assertIn("Elemento (0,1) = 2", output)
        self.assertIn("OPERACIONES CON MATRIZ COO", output)

if __name__ == '__main__':
    unittest.main()
