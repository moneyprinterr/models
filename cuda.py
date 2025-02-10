import torch
import sys

#commande pour lancer le serveur vllm
#installer vllm
#pip install vllm
#wsl
#python3 -m venv ~/venv_llm ou s'il est deja crée:
#   . ~/venv_llm/bin/activate.fish
#vllm serve deepseek-ai/DeepSeek-R1-Distill-Qwen-7B --tensor-parallel-size 2 --max-model-len 32768 --enforce-eager

def check_gpu():
    print(f"pytorch version: {torch.__version__}")
    print(f"python version: {sys.version}")
    
    print(f"\ncuda disponible: {torch.cuda.is_available()}")
    if not torch.cuda.is_available():
        print("aucun gpu cuda detecté!")
        return
    
    print(f"cuda version: {torch.version.cuda}")
    gpu_count = torch.cuda.device_count()
    print(f"\nnombre de gpus disponibles: {gpu_count}")

    for i in range(gpu_count):
        print(f"\ngpu {i}: {torch.cuda.get_device_name(i)}")
        print(f"- capacité de calcul: {torch.cuda.get_device_capability(i)}")
        

        mem_total = torch.cuda.get_device_properties(i).total_memory / 1024**3
        mem_reserved = torch.cuda.memory_reserved(i) / 1024**3
        mem_allocated = torch.cuda.memory_allocated(i) / 1024**3
        
        print(f"- mémoire totale: {mem_total:.2f} gb")
        print(f"- mémoire réservée: {mem_reserved:.2f} gb")
        print(f"- mémoire allouée: {mem_allocated:.2f} gb")
        print(f"- mémoire libre: {(mem_total - mem_reserved):.2f} gb")


if __name__ == "__main__":
    check_gpu()