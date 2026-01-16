# Neurons Engine

**Neurons Engine - Basic Component**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](https://github.com/qquartsco-svg/neurons-engine)
[![Status](https://img.shields.io/badge/status-commercial%20ready-green.svg)](https://github.com/qquartsco-svg/neurons-engine)

**Korean**: [README.md](README.md)

---

## 🎯 What It Does

**Neurons Engine** is an engine that provides neuron models, the basic components of neural networks.

**Core Components**:
- `CA3Neuron` - Hippocampal CA3 region neuron model
- `DGNeuron` - Dentate Gyrus neuron model
- `SpatialNeuron` - Spatial neuron model

---

## 🚀 Quick Start

### Installation

```bash
pip install -r requirements.txt
```

### Basic Usage

```python
from neurons import CA3Neuron

# Create CA3 neuron
neuron = CA3Neuron(
    neuron_id="CA3_0",
    baseline_V=-65.0,
    threshold=-31.5
)

# Update neuron
neuron.step(dt=0.1, I_total=10.0)
```

---

## 📁 Project Structure

```
neurons-engine/
├── neurons/
│   ├── neurons.py          # CA3, DG neuron models
│   ├── spatial_neurons.py  # Spatial neuron models
│   └── __init__.py
├── tests/                  # Tests
├── examples/               # Usage examples
├── docs/                   # Documentation
├── README.md               # This file (Korean)
├── README_EN.md            # English version
├── LICENSE                 # MIT License
├── setup.py                # Package configuration
└── requirements.txt        # Dependencies
```

---

## 🔬 Technical Background

### CA3 Neuron
- **Biological Basis**: Hippocampal CA3 region
- **Features**: STDP learning, Homeostasis, Recurrent connections
- **Usage**: Pattern completion, state maintenance

### DG Neuron
- **Biological Basis**: Dentate Gyrus
- **Features**: Pattern separation, sparse representation
- **Usage**: Input preprocessing

---

## 📝 License

**MIT License** - See `LICENSE` file for details

---

## 💰 Revenue Sharing

For code reuse revenue sharing principles, see `REVENUE_SHARING.md`.

---

## 🔐 Blockchain Hash Record

This project uses blockchain hash records to prove:
- Public release: Technology is publicly available (no patents)
- Integrity: Files are unchanged (SHA-256 hashes)
- Precedence: Technical precedence can be proven

**Hash Record**: See `BLOCKCHAIN_HASH_RECORD.md`

---

**Last Updated**: 2026-01-17  
**Version**: v1.0.0

