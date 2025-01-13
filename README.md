# Fluxion

### Disrupting Reservoir Simulation

Fluxion is more than just a reservoir simulator—it’s a **state-of-the-art, open-source tool** designed to revolutionize how engineers interact with subsurface models. We are building the **next generation of reservoir simulation**, making high-performance modeling **accessible, intuitive, and seamlessly integrable** with modern data science tools.

### Why Fluxion?
- **Intuitive API:** Say goodbye to clunky, outdated syntax. Fluxion is built for the modern engineer.
- **Scalability:** Whether modeling a single well or a massive field, Fluxion adapts to your needs.
- **Visualization-First Approach:** Real-time 3D reservoir insights.
- **Seamless Integration:** Works alongside open-source libraries like pandas, scipy, and PyVista.
- **Open & Extensible:** Built with collaboration and future-proofing in mind.

## Installation
```bash
pip install fluxion
```

## Usage
```python
import fluxion as flx

grid = flx.Grid(10, 10, 10, 1, 1, 1)
well = flx.Well("Well-1", 100, 200, 300)
```