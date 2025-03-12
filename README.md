# Benchmark de Hardware 🖥️⚡

Este é um programa de benchmark para testar o desempenho de CPU, RAM, armazenamento e GPU do seu computador, utilizando **Python** e **Tkinter** para a interface gráfica.

## 📌 Funcionalidades
- Teste de CPU: Calcula operações matemáticas complexas para medir o desempenho.
- Teste de RAM: Mede a velocidade de manipulação da memória.
- Teste de Armazenamento: Mede a velocidade de leitura e escrita no disco.
- Teste de GPU: Simula processamento gráfico para estimar a performance.
- Interface gráfica intuitiva com gráficos para exibição dos resultados.

## 🛠️ Tecnologias Utilizadas
- **Python** (3.x)
- **Tkinter** (interface gráfica)
- **Matplotlib** (gráficos)
- **OpenCV** (teste de GPU)
- **Psutil** (monitoramento do sistema)

## 🚀 Como Executar

### 1️⃣ Instalar as Dependências
Certifique-se de ter o Python instalado e execute:
```bash
pip install -r requirements.txt
```

### 2️⃣ Rodar o Programa
```bash
python benchmark.py
```

### 3️⃣ Gerar um Executável (.exe)
Para criar um arquivo **.exe** no Windows:
```bash
pip install auto-py-to-exe
auto-py-to-exe
```
- Selecione o arquivo `benchmark.py`
- Marque a opção **Onefile**
- Marque **Windowed** (para não abrir terminal)
- Adicione o ícone **gauge_chart.ico** (opcional)
- Clique em **Convert .py to .exe**

Alternativamente, use o PyInstaller:
```bash
pyinstaller --onefile --windowed --icon=gauge_chart.ico benchmark.py
```
O executável estará na pasta `dist/`.

## 🎨 Personalização
Para alterar o ícone do executável, substitua `gauge_chart.ico` no código e na conversão para `.exe`.

## 📜 Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para modificar e distribuir. 😊

---
💡 **Dica**: Teste o programa em diferentes máquinas para comparar desempenhos! 🔥

