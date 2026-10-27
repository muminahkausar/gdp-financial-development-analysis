"""Visualise reported coursework regression statistics; no OLS is estimated."""
from pathlib import Path
import matplotlib.pyplot as plt

MODELS = ["GDPC only", "GDPC + income indicator"]
ADJUSTED_R2 = [0.171, 0.211]
GDPC_P_VALUES = [0.0047, 0.411]

fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].bar(MODELS, ADJUSTED_R2)
axes[0].set_ylabel("Adjusted R²")
axes[0].set_title("Reported model fit")
axes[0].set_ylim(0, 0.26)
axes[1].bar(MODELS, GDPC_P_VALUES)
axes[1].axhline(0.05, linestyle="--", linewidth=1, label="5% threshold")
axes[1].set_ylabel("P-value for GDPC coefficient")
axes[1].set_title("Reported statistical significance")
axes[1].legend()
for ax in axes:
    ax.tick_params(axis="x", labelrotation=15)
fig.suptitle("Comparison of coursework regression summaries")
fig.tight_layout()
out = Path(__file__).resolve().parents[1] / "figures" / "model_comparison.png"
fig.savefig(out, dpi=180, bbox_inches="tight")
print(f"Saved {out}")
