from glisco.plone6.extensions.vocabularies.constants import (
    THEMES_TAXONOMY,
    SITE_ARCHETYPES_TAXONOMY
)

THEMES_DATA = [
    {
        "token": THEMES_TAXONOMY + ".futuristic", #Futuristic	Cutting-edge, sleek, bold motion	Neon accents, dark/light contrast, geometric type
        "titles": {
            "en": "Futuristic",
            "pt": "Futurista",
        },
    },
    {
        "token": THEMES_TAXONOMY + ".visionary", # Visionary	Aspirational, elegant, innovative	Soft gradients, serif+sans pairings, storytelling feel
        "titles": {
            "en": "Visionary",
            "pt": "Visionário",
        },
    },
    {
        "token": THEMES_TAXONOMY + ".modern", # Modern	Clean, flat, businesslike	Clear layout, minimal decoration, bold sans-serif
        "titles": {
            "en": "Modern",
            "pt": "Moderno",
        },
    },

    {
        "token": THEMES_TAXONOMY + ".executive", # Executive	Premium, refined, high-end corporate	Dark tones, fine typography, prestige vibe
        "titles": {
            "en": "Executive",
            "pt": "Executivo",
        },
    },

    {
        "token": THEMES_TAXONOMY + ".conservative", # Conservative	Formal, classic, trust-first	Structured grids, serif fonts, restrained color
        "titles": {
            "en": "Conservative",
            "pt": "Conservador",
        },
    },

    {
        "token": THEMES_TAXONOMY + ".minimal", # Minimal     Uncluttered, spacious, focus-first	White space, simple lines, few elements
        "titles": {
            "en": "Minimal",
            "pt": "Minimal",
        },
    },


    {
        "token": THEMES_TAXONOMY + ".neutral", # Neutral	Functional, minimal, adaptable	Muted colors, lots of whitespace, system feel
        "titles": {
            "en": "Neutral",
            "pt": "Neutro",
        },
    },   

]

SITE_ARCHETYPES = [
    {
        "token": SITE_ARCHETYPES_TAXONOMY + ".catalog", # Catalog-Driven	Surface browsable product listings	Ecommerce, Real Estate, Marketplaces	Grid/List views, filters, product cards, featured picks, CTAs
        "titles": {
            "en": "Catalog-Driven",
            "pt": "Catálogo",
        },
    },

    {
        "token": SITE_ARCHETYPES_TAXONOMY + ".casestudy", # Case-Study-Driven	Build trust via past success	Consulting, B2B Services, Agencies	Hero → Challenge → Solution → Results → Quote → CTA
        "titles": {
            "en": "Case Study-Driven",
            "pt": "Estudo de Caso",
        },
    },

    {
        "token": SITE_ARCHETYPES_TAXONOMY + ".funnel", # Sales Page / Funnel	Guide visitor to convert	SaaS, Online Services, Courses	Benefit stack, objections-handling FAQ, social proof, pricing
        "titles": {
            "en": "Sales Page / Funnel",
            "pt": "Página de Vendas / Funil",
        },
    },

    {
        "token": SITE_ARCHETYPES_TAXONOMY + ".authority", # Authority-Led	Establish thought leadership	Law, Finance, Advisory, NGOs	Articles, whitepapers, author bios, deep content, email capture
        "titles": {
            "en": "Authority-Led",
            "pt": "Autoridade",
        },
    },

    {
        "token": SITE_ARCHETYPES_TAXONOMY + ".directory", # Directory-Based	Organise many entries	Health clinics, member orgs, events, education	Searchable list, filters, detail views, maps
        "titles": {
            "en": "Directory-Based",
            "pt": "Diretório",
        },
    },

    {
        "token": SITE_ARCHETYPES_TAXONOMY + ".event", # Event-Driven	Drive attendance or awareness	Conferences, campaigns, launches	Countdown, program schedule, speaker bios, register CTA
        "titles": {
            "en": "Event-Driven",
            "pt": "Dirigido por Eventos",
        },
    },

    {
        "token": SITE_ARCHETYPES_TAXONOMY + ".portfolio", # Portfolio-Led	Showcase creative work	Creative studios, architects, freelancers	Image-led grid, project narratives, awards, testimonials
        "titles": {
            "en": "Portfolio-Led",
            "pt": "Portfólio",
        },
    },

    {
        "token": SITE_ARCHETYPES_TAXONOMY + ".booking", # Booking-Based	Drive scheduling of services	Wellness, Clinics, Coaching	Service list, time slots, availability calendar, booking form
        "titles": {
            "en": "Booking-Based",
            "pt": "Baseado em Reservas",
        },
    },

    {
        "token": SITE_ARCHETYPES_TAXONOMY + ".hybrid", # Hybrid (Mixed)	Combine models flexibly	Larger businesses or layered offerings	Mix of catalog + case studies + articles
        "titles": {
            "en": "Hybrid (Mixed)",
            "pt": "Híbrido (Misto)",
        },
    },

]