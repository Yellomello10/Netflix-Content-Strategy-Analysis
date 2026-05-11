from __future__ import annotations

from pathlib import Path
from typing import Iterable

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


PLOT_STYLE = {
    "axes.facecolor": "#f8f6f1",
    "figure.facecolor": "#fcfaf7",
    "axes.edgecolor": "#323232",
    "axes.labelcolor": "#1f1f1f",
    "text.color": "#1f1f1f",
    "xtick.color": "#1f1f1f",
    "ytick.color": "#1f1f1f",
    "grid.color": "#d9d2c7",
}

PALETTE = ["#e50914", "#b20710", "#221f1f", "#564d4d", "#b81d24", "#f5f5f1"]


def set_plot_style() -> None:
    sns.set_theme(style="whitegrid", palette=PALETTE)
    plt.rcParams.update(PLOT_STYLE)
    plt.rcParams.update({
        "figure.figsize": (12, 7),
        "axes.titleweight": "bold",
        "axes.titlesize": 16,
        "axes.labelsize": 12,
    })


def save_figure(fig: plt.Figure, output_path: str | Path | None = None) -> None:
    if output_path is None:
        return
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, bbox_inches="tight", dpi=160)


def plot_pie(series: pd.Series, title: str, output_path: str | Path | None = None) -> plt.Axes:
    set_plot_style()
    fig, ax = plt.subplots()
    colors = PALETTE[: len(series)]
    ax.pie(series.values, labels=series.index, autopct="%1.1f%%", startangle=90, colors=colors)
    ax.set_title(title)
    ax.axis("equal")
    save_figure(fig, output_path)
    return ax


def plot_horizontal_bar(frame: pd.DataFrame, x: str, y: str, title: str, output_path: str | Path | None = None) -> plt.Axes:
    set_plot_style()
    fig, ax = plt.subplots()
    ordered = frame.sort_values(x, ascending=True)
    sns.barplot(data=ordered, x=x, y=y, ax=ax, palette=PALETTE)
    ax.set_title(title)
    ax.set_xlabel(x.replace("_", " ").title())
    ax.set_ylabel(y.replace("_", " ").title())
    save_figure(fig, output_path)
    return ax


def plot_vertical_bar(frame: pd.DataFrame, x: str, y: str, title: str, output_path: str | Path | None = None) -> plt.Axes:
    set_plot_style()
    fig, ax = plt.subplots()
    sns.barplot(data=frame, x=x, y=y, ax=ax, palette=PALETTE)
    ax.set_title(title)
    ax.set_xlabel(x.replace("_", " ").title())
    ax.set_ylabel(y.replace("_", " ").title())
    plt.xticks(rotation=45, ha="right")
    save_figure(fig, output_path)
    return ax


def plot_line(frame: pd.DataFrame | pd.Series, title: str, ylabel: str, output_path: str | Path | None = None) -> plt.Axes:
    set_plot_style()
    fig, ax = plt.subplots()

    if isinstance(frame, pd.Series):
        frame.plot(ax=ax, linewidth=2.5, color=PALETTE[0])
        legend = ax.get_legend()
        if legend is not None:
            legend.remove()
    else:
        frame.plot(ax=ax, linewidth=2.0)

    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel(ylabel)
    if not isinstance(frame, pd.Series):
        legend = ax.get_legend()
        if legend is not None:
            legend.set_frame_on(True)
    save_figure(fig, output_path)
    return ax


def plot_heatmap(frame: pd.DataFrame, title: str, output_path: str | Path | None = None) -> plt.Axes:
    set_plot_style()
    fig, ax = plt.subplots(figsize=(14, 8))
    sns.heatmap(frame, cmap="Reds", linewidths=0.25, linecolor="#f0ebe3", ax=ax)
    ax.set_title(title)
    ax.set_xlabel("")
    ax.set_ylabel("")
    save_figure(fig, output_path)
    return ax
