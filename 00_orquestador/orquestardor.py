import subprocess
import sys
import gc
import os
from datetime import datetime

def install_dependencies():
    """
    Instala papermill si no está disponible en el entorno actual.
    """
    try:
        import papermill
        print("✓ papermill ya está instalado")
    except ImportError:
        print("⚙ Instalando papermill...")
        try:
            subprocess.check_call([
                sys.executable, '-m', 'pip', 'install', 
                'papermill', '--quiet'
            ])
            print("✓ papermill instalado exitosamente")
        except subprocess.CalledProcessError as e:
            print(f"✗ Error instalando papermill: {e}")
            sys.exit(1)

class NotebookOrchestrator:
    """
    Orquestador para ejecutar notebooks secuencialmente con limpieza de memoria.
    """
    
    def __init__(self, notebooks_path="../02_notebooks"):
        self.original_dir = os.getcwd()
        
        # Resolver la ruta correctamente desde donde se ejecuta el script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.notebooks_path = os.path.normpath(
            os.path.join(script_dir, notebooks_path)
        )
        
        # Crear carpeta de logs en el directorio del orquestador
        self.log_dir = os.path.join(script_dir, "logs")
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_file = os.path.join(
            self.log_dir, 
            f"orchestrator_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        )
        
    def log(self, message):
        """Registra mensajes en consola y archivo de log"""
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f"[{timestamp}] {message}"
        print(log_message)
        with open(self.log_file, 'a', encoding='utf-8') as f:
            f.write(log_message + '\n')
    
    def execute_notebook(self, notebook_name):
        """
        Ejecuta un notebook usando papermill en un proceso separado.
        Cambia al directorio de notebooks para que las rutas relativas funcionen.
        """
        input_path = os.path.join(self.notebooks_path, notebook_name)
        output_path = os.path.join(
            self.notebooks_path, 
            f"executed_{notebook_name}"
        )
        
        self.log(f"Iniciando ejecución de: {notebook_name}")
        
        # Guardar directorio actual
        current_dir = os.getcwd()
        
        try:
            # Cambiar al directorio de notebooks para que rutas relativas funcionen
            os.chdir(self.notebooks_path)
            self.log(f"Directorio de trabajo: {os.getcwd()}")
            
            # Ejecutar notebook en proceso separado
            cmd = [
                sys.executable, '-m', 'papermill',
                notebook_name,  # Ahora usamos solo el nombre, no la ruta completa
                f"executed_{notebook_name}",
                '--log-output',
                '--log-level', 'INFO'
            ]
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                check=True
            )
            
            self.log(f"✓ Completado exitosamente: {notebook_name}")
            return True
            
        except subprocess.CalledProcessError as e:
            self.log(f"✗ Error ejecutando {notebook_name}")
            self.log(f"Error: {e.stderr}")
            return False
        except Exception as e:
            self.log(f"✗ Error inesperado en {notebook_name}: {str(e)}")
            return False
        finally:
            # Volver al directorio original
            os.chdir(current_dir)
            # Forzar limpieza de memoria
            gc.collect()
            self.log(f"Memoria limpiada después de {notebook_name}")
            self.log(f"Volviendo al directorio: {current_dir}\n")
    
    def run_pipeline(self, notebooks):
        """
        Ejecuta la lista de notebooks secuencialmente.
        
        Args:
            notebooks: Lista de nombres de notebooks en orden de ejecución
        """
        self.log("="*60)
        self.log("INICIANDO PIPELINE DE NOTEBOOKS")
        self.log("="*60)
        
        total = len(notebooks)
        successful = 0
        
        for i, notebook in enumerate(notebooks, 1):
            self.log(f"\nProcesando notebook {i}/{total}")
            
            if self.execute_notebook(notebook):
                successful += 1
            else:
                self.log(f"\n⚠ Pipeline detenido debido a error en {notebook}")
                break
        
        # Resumen final
        self.log("\n" + "="*60)
        self.log("RESUMEN DE EJECUCIÓN")
        self.log("="*60)
        self.log(f"Notebooks ejecutados exitosamente: {successful}/{total}")
        
        if successful == total:
            self.log("✓ Pipeline completado exitosamente")
        else:
            self.log("✗ Pipeline completado con errores")
        
        return successful == total


def main():
    """
    Función principal para ejecutar el orquestador del proyecto DSMarket
    """
    # Instalar dependencias necesarias
    install_dependencies()
    
    # Notebooks del proyecto en orden de ejecución
    notebooks = [
        "01_DSMarket_data_preparation.ipynb",
        "02_DSMarket_Clustering.ipynb",
        "03_DSMarket_forecasting.ipynb",
        "04_DSMarket_SS_calculation.ipynb"
    ]
    
    # Crear y ejecutar orquestador
    # La ruta es relativa desde 00_orquestador/ hacia 02_notebooks/
    orchestrator = NotebookOrchestrator(notebooks_path="../02_notebooks")
    success = orchestrator.run_pipeline(notebooks)
    
    # Código de salida
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()