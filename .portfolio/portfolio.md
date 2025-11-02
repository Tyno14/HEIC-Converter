---
title: "HEIC Converter"
description: "Application graphique Python pour convertir des images .heic  vers .jpg, .png ou .webp. Localement"
date: "2025-06-25"
tags: ["python","gui","tkinter","pillow","heic"]
lang: "fr"

# Configuration techStack
techStack:
  - name: "Python"
    category: "language"
    icon: "🐍"
  - name: "Tkinter"
    category: "framework"
    icon: "🖼️"
  - name: "Pillow (PIL)"
    category: "tool"
    icon: "🎨"
  - name: "pillow-heif"
    category: "tool"
    icon: "🍏"
  - name: "tkinterdnd2"
    category: "tool"
    icon: "🖱️"
  - name: "PyInstaller"
    category: "tool"
    icon: "📦"

# Architecture du projet
architecture:
  overview: "L'application repose sur une architecture simple séparant la logique métier de l'interface utilisateur. Le module gui.py utilise Tkinter pour construire l'intégralité de la fenêtre graphique et gérer les interactions utilisateur (sélection de fichiers, drag-and-drop via tkinterdnd2). La conversion réelle des images est déléguée au module converter.py, qui utilise Pillow et pillow-heif pour traiter les fichiers en arrière-plan, évitant de bloquer l'interface."
  components:
    - "main.py (Point d'entrée) : Script minimal qui initialise et lance l'application. Il importe la classe App depuis src/gui.py et démarre la boucle principale Tkinter."
    - "src/gui.py (Classe App) : Le cœur de l'application. Cette classe hérite de TkinterDnD.Tk pour gérer la fenêtre principale et le drag-and-drop. Elle construit tous les widgets et gère l'état."
    - "src/converter.py (Classe Converter) : La logique métier pure. Gère le processus de conversion d'image (ouverture avec pillow-heif, sauvegarde avec Pillow) et la suppression optionnelle."
    - "Gestion du Threading : La méthode start_conversion (dans gui.py) lance le Converter dans un threading.Thread séparé pour empêcher l'interface de 'geler' (freeze)."
    - "Gestionnaire d'événements (Callbacks) : Ensemble des fonctions dans gui.py (ex: select_files, handle_drop) qui réagissent aux actions de l'utilisateur."

# Diagrammes d'architecture (optionnel)
diagrams:
  - path: "diagrams/github/diagram.svg"
    title: "Architecture applicative"
    description: "Vue d'ensemble de l'architecture GUI et logique métier"

# URLs et liens
demo_url: ""
demo_label: ""
github_repo: "Tyno14/HEIC-Converter"
github_url: "https://github.com/Tyno14/HEIC-Converter"
github_stars: 0
github_language: "Python"
---

## 🎯 Vue d'ensemble

<div class="overview-hero dark:bg-gradient-to-br dark:from-accent/10 dark:to-purple-900/10 bg-gradient-to-br from-indigo-50 to-purple-50 border dark:border-accent/20 border-indigo-200 rounded-2xl p-8 my-8 shadow-lg">
  <p class="text-lg dark:text-white/90 text-slate-700 leading-relaxed mb-6">
    HEIC Converter est un utilitaire de bureau <strong>simple</strong> et <strong>efficace</strong> conçu pour une seule tâche : libérer vos photos du format `.heic`. Il permet une conversion <strong>100% locale</strong> vers les formats JPG, PNG ou WEBP, garantissant que vos images personnelles ne quittent <strong>jamais</strong> votre ordinateur. L'interface claire et le support du <strong>glisser-déposer</strong> rendent le processus de conversion rapide et intuitif pour tous.
  </p>
  
  <div class="stats-row grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">3</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Formats supportés</div>
    </div>
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">2</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Installeurs natifs</div>
    </div>
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">100%</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Traitement local</div>
    </div>
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">23.2 Mo</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Poids de l'app</div>
    </div>
  </div>
</div>

### Objectifs du projet

<div class="objectives-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🔒
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Confidentialité Totale
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Garantir un traitement 100% local. Aucune photo n'est envoyée sur Internet, résolvant le problème de confidentialité des convertisseurs en ligne.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🎯
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Efficacité et Simplicité
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Fournir un outil "drag-and-drop" qui va droit au but. L'interface doit être minimale et le processus de conversion immédiat.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🧠
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Montée en Compétence (Projet Perso)
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Mettre en pratique les compétences en Python, de la création d'une GUI (Tkinter) à la manipulation de bibliothèques tierces et au packaging.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🔄
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Solution Multi-Format
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Résoudre le problème de compatibilité du format `.heic` en proposant les trois formats de sortie les plus universels (JPG, PNG, WEBP).
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🛡️
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Application "Privacy by Design"
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      En tant qu'étudiant en sécurité, créer un outil qui incarne ce principe. Pas de collecte de données, pas de connexion réseau, juste le code nécessaire.
    </p>
  </div>
</div>

## ⚛️ Interface Graphique (GUI) avec Tkinter

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    L'interface est entièrement construite avec la bibliothèque Python native <strong>Tkinter</strong>, en utilisant les widgets modernes de <strong>`ttk`</strong> pour une apparence soignée. La fonctionnalité clé de <strong>glisser-déposer</strong> est implémentée grâce à la bibliothèque `tkinterdnd2`, rendant l'ajout de fichiers intuitif.
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Fenêtre principale (Root) :</strong> La classe <code>App</code> hérite de <code>TkinterDnD.Tk</code> pour servir de fenêtre racine acceptant les fichiers déposés.</li>
    <li><strong>Panneau de contrôle :</strong> Utilisation de <code>ttk.Frame</code> pour organiser les widgets : <code>ttk.Combobox</code> pour le choix du format et <code>ttk.Checkbutton</code> pour l'option de suppression.</li>
    <li><strong>Liste de fichiers :</strong> Une <code>tk.Listbox</code> centrale affiche tous les fichiers <code>.heic</code> en attente, couplée à une <code>ttk.Scrollbar</code>.</li>
    <li><strong>Gestion des événements :</strong> Implémentation de <code>handle_drop</code> (drag-and-drop) et <code>select_files</code> (dialogue natif) pour peupler la liste de fichiers.</li>
    <li><strong>Feedback utilisateur :</strong> Une <code>ttk.Progressbar</code> et un <code>ttk.Label</code> de statut informent l'utilisateur en temps réel de l'avancement.</li>
  </ul>
</div>

## ⚙️ Moteur de Conversion Asynchrone

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    Pour garantir une interface réactive, la conversion n'est <strong>pas</strong> exécutée sur le thread principal. Un <strong>thread dédié</strong> est lancé pour gérer le traitement lourd des images, permettant à l'utilisateur de continuer à interagir avec l'application sans qu'elle ne "gèle".
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong><code>threading.Thread</code> :</strong> La méthode <code>start_conversion</code> (dans <code>gui.py</code>) instancie un <code>threading.Thread</code> qui cible la méthode <code>converter.run</code>.</li>
    <li><strong>Bibliothèque <code>pillow-heif</code> :</strong> La bibliothèque critique qui décode le format <code>.heif</code>/<code>.heic</code> (non supporté par Pillow seul).</li>
    <li><strong>Bibliothèque <code>Pillow (PIL)</code> :</strong> Une fois l'image ouverte, Pillow gère la sauvegarde (<code>.save()</code>) vers les formats de destination (JPG, PNG, WEBP).</li>
    <li><strong>Gestion de l'état (State Management) :</strong> L'interface désactive les boutons (<code>state="disabled"</code>) et affiche la barre de progression pendant que le thread de conversion s'exécute.</li>
  </ul>
</div>

## 📦 Packaging et Distribution

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    L'objectif était de fournir une application <strong>"clés en main"</strong> ne nécessitant pas l'installation de Python. Le projet est donc packagé dans des formats natifs pour Windows et Linux (Debian/Ubuntu).
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Exécutable Windows (<code>.exe</code>) :</strong> Un binaire unique pour Windows (probablement créé avec <strong>PyInstaller</strong>) qui embarque l'interpréteur Python et toutes les dépendances.</li>
    <li><strong>Paquet Debian (<code>.deb</code>) :</strong> Un paquet <code>.deb</code> est généré pour les distributions basées sur Debian (Ubuntu, Mint).</li>
    <li><strong>GitHub Releases :</strong> Les binaires compilés sont hébergés directement sur la page "Releases" du dépôt GitHub, servant de point de téléchargement centralisé.</li>
    <li><strong>Indépendance :</strong> Les deux méthodes de packaging garantissent que l'application s'exécute en "standalone", sans que l'utilisateur n'ait à se soucier des <code>pip install</code>.</li>
  </ul>
</div>

## 🎓 Compétences démontrées

<div class="skills-showcase space-y-6 my-8">
  
  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🐍</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">Développement Backend & Logique</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Programmation asynchrone</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Utilisation de `threading` pour une conversion non-bloquante.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Manipulation de formats non-natifs</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Intégration de `pillow-heif` pour lire les images `.heic`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Traitement d'images</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Utilisation de `Pillow (PIL)` pour la sauvegarde en JPG, PNG, WEBP.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Conception Orientée Objet (OOP)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Encapsulation de la logique métier dans la classe `Converter`.</div>
        </div>
      </div>
    </div>
  </div>
  
  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🖼️</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">Développement Interface (GUI)</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Construction d'interface (GUI) native</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Utilisation de `Tkinter` et des widgets modernes `ttk`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Implémentation du "Drag-and-Drop"</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Intégration de la bibliothèque `tkinterdnd2`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Communication inter-thread</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Passage de "callback" de la GUI au thread de conversion.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Gestion de l'état de l'interface</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Désactivation (`state="disabled"`) des widgets pendant le traitement.</div>
        </div>
      </div>
    </div>
  </div>

  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">📦</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">DevOps & Packaging</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Packaging "Standalone"</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Création d'exécutables (`.exe`) pour Windows (PyInstaller).</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Création de paquets Linux</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Génération de paquets `.deb` pour systèmes Debian/Ubuntu.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Gestion des dépendances</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Définition d'un environnement via `requirements.txt`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Distribution de version (Release)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Publication des binaires compilés via GitHub Releases.</div>
        </div>
      </div>
    </div>
  </div>

</div>

## 📚 Ressources & Documentation

<div class="documentation-grid grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
  
  <div class="doc-card dark:bg-gradient-to-br dark:from-slate-900/50 dark:to-slate-800/50 bg-gradient-to-br from-slate-50 to-slate-100 border dark:border-white/10 border-slate-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300 cursor-pointer" data-doc-type="details">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">📖</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Documentation complète</h3>
    </div>
    <ul class="space-y-3">
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Analyse du code source Python</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Logique de l'interface (Tkinter)</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Processus de conversion (Pillow)</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Instructions de packaging (.exe/.deb)</span>
      </li>
    </ul>
    <div class="mt-4 text-center">
      <span class="text-sm dark:text-blue-400 text-blue-600 font-semibold">→ Voir les détails techniques</span>
    </div>
  </div>

  <div class="doc-card dark:bg-gradient-to-br dark:from-purple-900/30 dark:to-indigo-900/30 bg-gradient-to-br from-purple-50 to-indigo-50 border dark:border-purple-500/30 border-purple-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300 cursor-pointer" data-doc-type="architecture">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🗺️</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Diagramme interactif</h3>
    </div>
    <p class="dark:text-white/70 text-slate-600 mb-4">Visualisation complète de l'architecture avec tooltips détaillés pour chaque composant.</p>
    <div class="flex flex-wrap gap-2 mb-4">
      <span class="px-3 py-1 dark:bg-blue-500/20 bg-blue-200 dark:text-blue-300 text-blue-700 rounded-full text-xs">Interface (GUI)</span>
      <span class="px-3 py-1 dark:bg-red-500/20 bg-red-200 dark:text-red-300 text-red-700 rounded-full text-xs">Logique (Backend)</span>
      <span class="px-3 py-1 dark:bg-purple-500/20 bg-purple-200 dark:text-purple-300 text-purple-700 rounded-full text-xs">Threading</span>
      <span class="px-3 py-1 dark:bg-green-500/20 bg-green-200 dark:text-green-300 text-green-700 rounded-full text-xs">Packaging</span>
    </div>
    <div class="text-center">
      <span class="text-sm dark:text-purple-400 text-purple-600 font-semibold">→ Voir l'architecture</span>
    </div>
  </div>

</div>

<script is:inline>
  document.addEventListener('DOMContentLoaded', function() {
    const docCards = document.querySelectorAll('[data-doc-type]');
    docCards.forEach(card => {
      card.addEventListener('click', function() {
        const type = this.getAttribute('data-doc-type');
        const tabButton = document.querySelector(`[data-tab="${type}"]`);
        if (tabButton) {
          tabButton.click();
        }
      });
    });
  });
</script>

---

**Archivé** | **Application Bureau** | **Projet Personnel**
