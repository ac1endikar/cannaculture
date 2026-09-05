// CannaCatalog 2.0 MAX - Herramientas Avanzadas (Mezclador, Comparador, Vaporización & Temas)

import { STRAINS_DATABASE, TERPENES_INFO } from './data.js?v=2026_clean_v45';

export class AdvancedTools {

  /* ----------------------------------------------------
     1. COMPARADOR DE CEPAS FRENTE A FRENTE
     ---------------------------------------------------- */
  static compareStrains(strainId1, strainId2) {
    const s1 = STRAINS_DATABASE.find(s => s.id === strainId1);
    const s2 = STRAINS_DATABASE.find(s => s.id === strainId2);

    if (!s1 || !s2) return null;

    return {
      strain1: s1,
      strain2: s2,
      thcDiff: s1.thc - s2.thc,
      cbdDiff: s1.cbd - s2.cbd,
      terpeneMatch: s1.dominantTerpene === s2.dominantTerpene
    };
  }

  /* ----------------------------------------------------
     2. MEZCLADOR DE CEPAS (SALAD BOWL BLENDER)
     ---------------------------------------------------- */
  static blendStrains(strainId1, strainId2, ratio1 = 50) {
    const s1 = STRAINS_DATABASE.find(s => s.id === strainId1) || STRAINS_DATABASE[0];
    const s2 = STRAINS_DATABASE.find(s => s.id === strainId2) || STRAINS_DATABASE[1];

    const r1 = ratio1 / 100;
    const r2 = 1 - r1;

    const blendedThc = (s1.thc * r1 + s2.thc * r2).toFixed(1);
    const blendedCbd = (s1.cbd * r1 + s2.cbd * r2).toFixed(1);

    return {
      name: `Blend Custom (${s1.name} + ${s2.name})`,
      ratioText: `${ratio1}% ${s1.name} / ${100 - ratio1}% ${s2.name}`,
      thc: blendedThc,
      cbd: blendedCbd,
      combinedEffects: Array.from(new Set([...s1.effects, ...s2.effects])),
      combinedFlavors: Array.from(new Set([...s1.flavors, ...s2.flavors])),
      dominantTerpenes: [s1.dominantTerpene, s2.dominantTerpene]
    };
  }

  /* ----------------------------------------------------
     3. TABLA DE TEMPERATURAS DE VAPORIZACIÓN
     ---------------------------------------------------- */
  static getVapeTemps() {
    return [
      { terpene: "Cariofileno", tempC: 130, tempF: 266, effect: "Alivio físico & Anti-ansiedad", color: "#EF4444" },
      { terpene: "Humuleno",    tempC: 106, tempF: 223, effect: "Supresor apetito & Calmante",  color: "#A78BFA" },
      { terpene: "Pineno",      tempC: 155, tempF: 311, effect: "Claridad mental & Enfoque láser", color: "#06B6D4" },
      { terpene: "Mirceno",     tempC: 167, tempF: 333, effect: "Relajación muscular & Calma profunda", color: "#10B981" },
      { terpene: "Limoneno",    tempC: 176, tempF: 349, effect: "Euforia & Elevación del ánimo", color: "#F59E0B" },
      { terpene: "Terpinoleno", tempC: 186, tempF: 367, effect: "Creatividad & Estimulación cognitiva", color: "#EC4899" },
      { terpene: "Linalool",    tempC: 198, tempF: 388, effect: "Sueño reparador & Paz emocional", color: "#8B5CF6" },
      { terpene: "Ocimeno",     tempC: 66,  tempF: 151, effect: "Antiviral & Energía suave tropical", color: "#34D399" }
    ];
  }

  /* ----------------------------------------------------
     4b. ESTADÍSTICAS DEL CATÁLOGO
     ---------------------------------------------------- */
  static getCatalogStats(strains) {
    if (!strains || strains.length === 0) return null;
    const parseYield = y => typeof y === 'number' ? y : (parseInt(y) || 0);
    const banks = [...new Set(strains.map(s => s.bank))].length;
    const indicas = strains.filter(s => s.species === 'Indica').length;
    const sativas = strains.filter(s => s.species === 'Sativa').length;
    const hibridas = strains.filter(s => s.species === 'Híbrida' || s.species === 'Hibrida').length;
    const avgThc = (strains.reduce((sum, s) => sum + (typeof s.thc === 'number' ? s.thc : parseFloat(s.thc) || 0), 0) / strains.length).toFixed(1);
    const maxYieldIndoor = Math.max(...strains.map(s => parseYield(s.yieldIndoor)));
    const maxYieldOutdoor = Math.max(...strains.map(s => parseYield(s.yieldOutdoor)));
    const topRated = strains.slice().sort((a,b) => b.rating - a.rating)[0];
    return { total: strains.length, banks, indicas, sativas, hibridas, avgThc, maxYieldIndoor, maxYieldOutdoor, topRated };
  }

  /* ----------------------------------------------------
     4. GESTOR DE TEMAS DE COLOR (THEME ENGINE)
     ---------------------------------------------------- */
  static setTheme(themeName) {
    const root = document.documentElement;

    const themes = {
      emerald: {
        '--primary-emerald': '#10B981',
        '--primary-emerald-hover': '#059669',
        '--accent-purple': '#8B5CF6'
      },
      cyberpurple: {
        '--primary-emerald': '#8B5CF6',
        '--primary-emerald-hover': '#7C3AED',
        '--accent-purple': '#EC4899'
      },
      sunsetgold: {
        '--primary-emerald': '#F59E0B',
        '--primary-emerald-hover': '#D97706',
        '--accent-purple': '#EF4444'
      },
      obsidian: {
        '--primary-emerald': '#06B6D4',
        '--primary-emerald-hover': '#0891B2',
        '--accent-purple': '#10B981'
      }
    };

    const targetTheme = themes[themeName] || themes.emerald;
    Object.entries(targetTheme).forEach(([varName, val]) => {
      root.style.setProperty(varName, val);
    });

    localStorage.setItem('cannacatalog_theme', themeName);
  }
}
