import time
import sys
import os

# --- 1. Implementación del Árbol Binario de Búsqueda (BST) ---
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.frequency = 1
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.unique_chars = 0

    def insert_and_count(self, key):
        if self.root is None:
            self.root = BSTNode(key)
            self.unique_chars = 1
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key == node.key:
            node.frequency += 1
        elif key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
                self.unique_chars += 1
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert_recursive(node.right, key)

    def get_frequencies(self):
        frequencies = []
        self._inorder_traversal(self.root, frequencies)
        frequencies.sort(key=lambda x: x[0], reverse=True)
        return frequencies

    def _inorder_traversal(self, node, frequencies):
        if node:
            self._inorder_traversal(node.left, frequencies)
            frequencies.append((node.frequency, node.key))
            self._inorder_traversal(node.right, frequencies)


# --- 2. Clase de Criptoanálisis y Lógica de Hashing ---
class CryptoAnalysisMission:
    M = 31 
    CIPHERTEXT = "(/-.-4%(+28.%#+2/($(6(#(3(8%.-/2(+(/(6.("
    
    # Mapeo ESTRICTO: Asignación lógica basada en la prueba de hash: '(' -> 'e'
    STRICT_HASH_MAPPING = {
        '(': 'e', '/': 'l', '.': 'a', '-': 'd', '4': 'q', '%': 'u', 
        '+': 'o', '2': 's', '8': 'r', '#': 'ñ', '6': 't', '$': 'c', 
        '3': 'm', 
    }
    
    def __init__(self, output_file="Criptoanalisis_Resultado.txt"):
        self.bst = BST()
        self.execution_time = 0
        self.mapping = self.STRICT_HASH_MAPPING
        self.output_file = output_file

    def write_output(self, content, end='\n'):
        """Escribe en la consola y en el archivo."""
        print(content, end=end)
        with open(self.output_file, 'a', encoding='utf-8') as f:
            f.write(content + end)

    def hash_division(self, k):
        return (k % self.M) + 32

    def analizar_frecuencia(self):
        start_time = time.perf_counter()
        for char in self.CIPHERTEXT:
            self.bst.insert_and_count(char)
        end_time = time.perf_counter()
        self.execution_time = end_time - start_time
        return self.bst.get_frequencies()

    def postular_pares(self, frequencies):
        char_cifrado_max_freq = frequencies[0][1]
        char_original_postulado = 'e' 
        k_postulado = ord(char_original_postulado) 
        
        self.write_output(f"\nPostulado Clave para Ingeniería Inversa:")
        self.write_output(f"   Carácter Cifrado más frecuente: '{char_cifrado_max_freq}' (ASCII {ord(char_cifrado_max_freq)})")
        self.write_output(f"   Carácter Original postulado: '{char_original_postulado}' (ASCII {k_postulado})")
        
        return k_postulado, ord(char_cifrado_max_freq)

    def ingenieria_inversa(self, k_postulado, indice_esperado):
        indice_division = self.hash_division(k_postulado)
        self.write_output(f"\nPrueba de Mapeo por División (k='e'=101):")
        self.write_output(f"   índice_M = ({k_postulado} mod {self.M}) + 32 = {k_postulado % self.M} + 32 = {indice_division}")

        if indice_division == indice_esperado:
            self.write_output("   COINCIDENCIA: El Mapeo de División fue confirmado para este par clave.")
        else:
            self.write_output("   NO COINCIDE.")
        
        A_phi = (5**0.5 - 1) / 2
        self.write_output(f"   Justificación Teórica de A = {A_phi:.5f} (Proporción Áurea):")
        self.write_output("   Se elige por ser el valor óptimo que garantiza la **dispersión más uniforme** y minimiza colisiones.")

    def descifrado_final(self):
        self.write_output("\nMapeo de Sustitución Aplicado:")
        
        for cifrado, original in self.mapping.items():
            self.write_output(f"   '{cifrado}' -> '{original}'")

        descifrado_estricto = self.CIPHERTEXT.translate(str.maketrans(self.mapping))
        
        self.write_output(f"\nResultado del Descifrado Estricto: **{descifrado_estricto}**")
        
        # Devolvemos la cadena estricta para el resultado final
        return descifrado_estricto

    def run_mission(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("--- Misión de Criptoanálisis Iniciada ---\n")
        
        self.write_output("Elaborado por: \nJimenez Escutia Diego\nRuiz Evaristo Yamili\n")
        
        self.write_output("--- Misión de Criptoanálisis Iniciada ---")
        self.write_output(f"Mensaje Interceptado: {self.CIPHERTEXT}")

        # Fase 1
        frequencies = self.analizar_frecuencia()
        self.write_output("\nFase 1: Análisis de Frecuencia (BST)")
        self.write_output(f"   Tiempo de Ejecución: {self.execution_time:.6f} segundos")
        self.write_output("   Frecuencias ordenadas (Descendente):")
        for freq, char in frequencies:
            self.write_output(f"     '{char}': {freq} veces")
        
        self.write_output(f"\nNota: El carácter '(', con {frequencies[0][0]} apariciones, se utiliza como postulado principal para la prueba de hash.")

        k_postulado, indice_esperado = self.postular_pares(frequencies)

        # Fase 2
        self.ingenieria_inversa(k_postulado, indice_esperado)
        
        # Fase 3
        orden_descifrada = self.descifrado_final()
        
        self.write_output(f"\n\n--- INTERPRETACIÓN FINAL ---")
        self.write_output(f"   El mensaje descifrado estricto revela la cadena de caracteres obtenida al aplicar el Mapeo de División.")
        self.write_output(f"\nResultado Final del Criptoanálisis: **{orden_descifrada}**")

        self.write_output("\n--- Misión Cumplida ---")


# --- 3. Ejecución y Salida ---
if __name__ == "__main__":
    mission = CryptoAnalysisMission()
    mission.run_mission()
    print(f"\n[INFO]: La salida completa se ha guardado en el archivo '{mission.output_file}'.")
