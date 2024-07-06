import subprocess
import logging

# Setup logging
logging.basicConfig(filename='pipeline.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def run_script(script_name):
    try:
        result = subprocess.run(['python', script_name], check=True, capture_output=True, text=True)
        logging.info(f"Successfully ran {script_name}: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running {script_name}: {e.stderr}")

def main():
    scripts = [
        'ingest_product_catalog.py',
        'ingest_customer_transactions.py',
        'process_product_sales_detail.py'
    ]
    
    for script in scripts:
        logging.info(f"Running script: {script}")
        run_script(script)

if _name_ == '_main_':
    main()
ingest_product_catalog.py