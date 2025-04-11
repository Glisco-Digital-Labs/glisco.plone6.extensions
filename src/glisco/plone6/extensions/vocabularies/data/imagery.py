from glisco.plone6.extensions.vocabularies.constants import PHOTOGRAPHY_TONES_TAXONOMY
from glisco.plone6.extensions.vocabularies.constants import IMAGE_TREATMENT_TAXONOMY
from glisco.plone6.extensions.vocabularies.constants import IMAGE_MOOD_DESCRIPTORS_TAXONOMY
from glisco.plone6.extensions.vocabularies.constants import ILLUSTRATION_TYPES_TAXONOMY

# Image Generation Taxonomies
# The idea is that we use a combination of these to engineer prompts:
# [Mood] + [Image Type] + [Treatment] + [Style Prompt]



# Photography Tones / Visual Storytelling Styles
PHOTOGRAPHY_TONES_DATA = [
    {
        "token": PHOTOGRAPHY_TONES_TAXONOMY + ".lifestyle",
        "description": "Real people in natural settings, storytelling-oriented",
        "titles": {
            "en": "Lifestyle",
            "pt": "Lifestyle",
        },
    },

    {
        "token": PHOTOGRAPHY_TONES_TAXONOMY + ".editorial",
        "description": "Fashion-magazine-like, dramatic lighting, minimal background",
        "titles": {
            "en": "Editorial",
            "pt": "Editorial",
        },
    },

    {
        "token": PHOTOGRAPHY_TONES_TAXONOMY + ".studioproduct",
        "description": "Studio product photography, clean background, isolated subject, sharp detail",
        "titles": {
            "en": "Studio Product",
            "pt": "Studio Product",
        },
    },

    {
        "token": PHOTOGRAPHY_TONES_TAXONOMY + ".documentary",
        "description": "Real people in natural settings, storytelling-oriented. Raw, candid, 'in the moment' photography",
        "titles": {
            "en": "Documentary",
            "pt": "Documentary",
        },
    },

    {
        "token": PHOTOGRAPHY_TONES_TAXONOMY + ".flatlay",
        "descrption": "Overhead shots of arranged items, common in eCommerce or food photography",
        "titles": {
            "en": "Flat Lay",
            "pt": "Flat Lay",
        },
    },

    {
        "token": PHOTOGRAPHY_TONES_TAXONOMY + ".conceptual",
        "description": "Symbolic or staged scenes to evoke emotion or metaphor. Artistic photography that conveys a concept or idea, often with surreal or abstract elements",
        "titles": {
            "en": "Conceptual",
            "pt": "Conceptual",
        },
    },

    {
        "token": PHOTOGRAPHY_TONES_TAXONOMY + ".surreal",
        "description": "Unnatural or dreamy, often AI-styled or abstract",
        "titles": {
            "en": "Surreal",
            "pt": "Surreal",
        },
    },

    {
        "token": PHOTOGRAPHY_TONES_TAXONOMY + ".urban",
        "description": "City settings, architectural lines, texture-heavy",
        "titles": {
            "en": "Street/Urban",
            "pt": "Street/Urban",
        },
    },   
]

ILLUSTRATION_TYPES_TAXONOMY_DATA = [
    {
        "token": ILLUSTRATION_TYPES_TAXONOMY + ".flatvector",
        "description": "2D, minimal shading, bold shapes, often with a flat color palette",
        "titles": {
            "en": "Flat Vector",
            "pt": "Flat Vector",
        },
    },

    {
        "token": ILLUSTRATION_TYPES_TAXONOMY + ".isometric",
        "description": "3D-like, 2D perspective",
        "titles": {
            "en": "Isometric",
            "pt": "Isométrico",
        },
    },

    {
        "token": ILLUSTRATION_TYPES_TAXONOMY + ".3dcartoon",
        "description": "Playful, rounded, Pixar-style",
        "titles": {
            "en": "3D Cartoon",
            "pt": "3D Cartoon",
        },
    },

    {
        "token": ILLUSTRATION_TYPES_TAXONOMY + ".sketchpencil",
        "description": "Hand-drawn, pencil-like, rough or whimsical",
        "titles": {
            "en": "Sketch / Pencil",
            "pt": "Esboço / Lápis",
        },
    },

    {
        "token": ILLUSTRATION_TYPES_TAXONOMY + ".minimallineart",
        "description": "Thin outlines, almost no fill",
        "titles": {
            "en": "Minimal Line Art",
            "pt": "Arte Linha Minimalista",
        },
    },

    {
        "token": ILLUSTRATION_TYPES_TAXONOMY + ".collagecutout",
        "description": "Magazine-style composition from fragments",
        "titles": {
            "en": "Collage / Cutout",
            "pt": "Colagem / Recorte",
        },
    },

    {
        "token": ILLUSTRATION_TYPES_TAXONOMY + ".surrealabstract",
        "description": "Dreamlike, abstract, often AI-generated.",
        "titles": {
            "en": "Surreal Abstract",
            "pt": "Surreal Abstrato",
        },
    },

    {
        "token": ILLUSTRATION_TYPES_TAXONOMY + ".papercut",
        "description": "Layered paper cutouts, often with depth and texture",
        "titles": {
            "en": "Papercut",
            "pt": "Recorte de Papel",
        },
    },
]

IMAGE_TREATMENT_TAXONOMY_DATA = [
    {
        "token": IMAGE_TREATMENT_TAXONOMY + ".duotone",
        "description": "Two colors, often with a gradient effect or brand colored ",
        "titles": {
            "en": "Duotone",
            "pt": "Duotone",
        },
    },

    {
        "token": IMAGE_TREATMENT_TAXONOMY + ".overlaygradient",
        "description": "Gradient overlay on top of the image",
        "titles": {
            "en": "Overlay Gradient",
            "pt": "Sobreposição de Gradiente",
        },
    },

    {
        "token": IMAGE_TREATMENT_TAXONOMY + ".blurrededgemask",
        "description": "Blurred edges to create a vignette effect",
        "titles": {
            "en": "Blurred Edge Mask",
            "pt": "Máscara de Borda Desfocada",
        },
    },

    {
        "token": IMAGE_TREATMENT_TAXONOMY + ".highcontrastmono",
        "description": "High contrast monochrome treatment, often black and white with strong shadows and highlights",
        "titles": {
            "en": "High Contrast Mono",
            "pt": "Mono Alto Contraste",
        },
    },

    {
        "token": IMAGE_TREATMENT_TAXONOMY + ".mutedtones",
        "description": "Soft, desaturated colors",
        "titles": {
            "en": "Muted Tones",
            "pt": "Tons Suaves",
        },
    },

    {
        "token": IMAGE_TREATMENT_TAXONOMY + ".glitch",
        "description": "Digital distortion, pixelated or corrupted look",
        "titles": {
            "en": "Glitch",
            "pt": "Glitch",
        },
    },

    {
        "token": IMAGE_TREATMENT_TAXONOMY + ".glitch",
        "description": "Digital distortion, pixelated or corrupted look",
        "titles": {
            "en": "Glitch",
            "pt": "Glitch",
        },
    },

    {
        "token": IMAGE_TREATMENT_TAXONOMY + ".graintexture",
        "description": "Grainy texture, often with a film-like quality",
        "titles": {
            "en": "Grain & Texture",
            "pt": "Textura de Grão",
        },
    },

    {
        "token": IMAGE_TREATMENT_TAXONOMY + ".halftonedots",
        "description": "Dot pattern effect, reminiscent of old printing techniques",
        "titles": {
            "en": "Halftone/Dots",
            "pt": "Meia-Tons/Pontos",
        },
    },

]

IMAGE_MOOD_DESCRIPTORS_DATA = [
    {
        "token": IMAGE_MOOD_DESCRIPTORS_TAXONOMY + ".airy",
        "description": "Light, open, and spacious feel. Often bright and uplifting",
        "titles": {
            "en": "Airy",
            "pt": "Arejado",
        },
    },
    {
        "token": IMAGE_MOOD_DESCRIPTORS_TAXONOMY + ".pastel",
        "description": "Soft, muted colors that create a gentle and calming effect",
        "titles": {
            "en": "Pastel",
            "pt": "Pastel",
        },
    },

    {
        "token": IMAGE_MOOD_DESCRIPTORS_TAXONOMY + ".vibrant",
        "description": "Bright and lively colors that evoke energy and excitement",
        "titles": {
            "en": "Vibrant",
            "pt": "Vibrante",
        },
    },

    {
        "token": IMAGE_MOOD_DESCRIPTORS_TAXONOMY + ".muted",
        "description": "Subdued colors that create a sophisticated and understated look",
        "titles": {
            "en": "Muted",
            "pt": "Suave",
        },
    },

    {
        "token": IMAGE_MOOD_DESCRIPTORS_TAXONOMY + ".darkmoody",
        "description": "Rich, deep colors that create a dramatic and intense atmosphere",
        "titles": {
            "en": "Dark & Moody",
            "pt": "Escuro & Sombrio",
        },
    },

    {
        "token": IMAGE_MOOD_DESCRIPTORS_TAXONOMY + ".neutralgreyscale",
        "description": "'Neutral' or 'Greyscale' colors that create a clean and modern look. Often black and white or monochromatic palettes.",
        "titles": {
            "en": "Neutral / Greyscale",
            "pt": "Neutro / Escala de Cinza",
        },
    },

    {
        "token": IMAGE_MOOD_DESCRIPTORS_TAXONOMY + ".futuristic",
        "description": "'Futuristic' colors that evoke a sense of innovation and technology. Often metallic or neon hues.",
        "titles": {
            "en": "'Futuristic'",
            "pt": "'Futurista'",
        },
    },

    {
        "token": IMAGE_MOOD_DESCRIPTORS_TAXONOMY + ".playful",
        "description": "'Playful' colors that are bright, fun, and whimsical. Often used in children's products or creative branding.",
        "titles": {
            "en": "'Playful'",
            "pt": "'Divertido'",
        },
    },
]