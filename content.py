"""Portfolio content, taken from Jobs future/master-cv/master-cv.md.

Edit this file to update the site. Keep it consistent with the master CV:
nothing here should claim more than the master CV does.
"""

NAME = "Dan Thien Nguyen, Ph.D."
ROLE = "Materials Scientist · Pacific Northwest National Laboratory"
HEADLINE = "Battery materials,<br>from prediction to prototype."
INTRO = (
    "Materials scientist with 10+ years developing battery materials from first synthesis "
    "to working prototype. Principal investigator on DOE- and industry-funded programs in "
    "solid-state batteries, electrolyte design, and electrochemical critical-metals recovery."
)
LOCATION = "Richland, WA, USA"
EMAIL = "ng.danthien@gmail.com"

# Add your profile URLs here; a link only appears on the page once it has a URL.
LINKS = {
    "Google Scholar": "https://scholar.google.com/citations?user=1jZG1nUAAAAJ&hl=en",
    "LinkedIn": "",
    "ORCID": "",
    "PNNL profile": "https://www.pnnl.gov/people/dan-thien-nguyen",
    "Paper PDFs": "https://drive.google.com/drive/folders/1SF50x6fES75W5l0_HQ98tFvbxmBPmVsP?usp=share_link",
}

STATS = [
    ("10+", "years in battery materials R&D"),
    ("6 mo", "from predicted electrolyte to working solid-state prototype"),
    ("5", "patents and patent applications, U.S. and Korea"),
    ("5", "funders as PI or key personnel: DOE BES, DOE OE, Microsoft, NRF, LDRD"),
]

EXPERIENCE = [
    {
        "org": "Pacific Northwest National Laboratory",
        "place": "Richland, WA",
        "roles": [("Materials Scientist", "May 2023 – Present"),
                  ("Postdoctoral Research Associate", "Jun 2021 – May 2023")],
        "projects": [
            {
                "title": "Accelerating Scientific Discovery with HPC and AI",
                "tag": "Principal Investigator · Microsoft",
                "points": [
                    "Led a multidisciplinary team in the synthesis and characterization of novel solid electrolytes for all-solid-state batteries.",
                    "Advanced from predicted electrolyte structures to a functional solid-state battery prototype in six months.",
                    "Gave feedback to the Microsoft computational team to improve materials screening, and evaluated the electrolytes for a Li-ion pilot line.",
                ],
            },
            {
                "title": "Solid-State Battery Development, Energy Storage Research Alliance",
                "tag": "Key personnel · DOE BES",
                "points": [
                    "Led synthesis and characterization of sodium metal oxyhalide and sodium thiophosphate superionic conductors.",
                    "Established characterization protocols for solid electrolytes and electrode interfaces in Na and Li batteries.",
                ],
            },
            {
                "title": "Long-Duration Energy Storage for Grid Applications",
                "tag": "Principal Investigator · DOE Office of Electricity",
                "points": [
                    "Designed an advanced cell architecture using slurry-based cathode and anode materials.",
                    "Ran a 3D CAD → 3D-printed prototype → electrochemical validation cycle; first working device in five months.",
                ],
            },
            {
                "title": "High-Efficiency Critical Metals Separation",
                "tag": "Principal Investigator · LDRD",
                "points": [
                    "Developed a circular electrochemical system to separate critical metals from end-of-life magnets.",
                    "Directed experimental design, data analysis, sponsor engagement, and IP development.",
                ],
            },
            {
                "title": "Surface Reactions in Non-Aqueous Rechargeable Batteries",
                "tag": "Key personnel · DOE BES",
                "points": [
                    "Used multimodal spectroscopy to resolve interfacial reactions at the electrode-electrolyte interface.",
                    "Correlated electrolyte properties with electrochemical performance and longevity.",
                ],
            },
        ],
    },
    {
        "org": "Institute of Materials Research and Engineering, A*STAR",
        "place": "Singapore",
        "roles": [("Scientist", "Apr 2018 – May 2021")],
        "projects": [
            {
                "title": "Electrolyte Additives for OCV Degradation in Commercial Li-ion Batteries",
                "tag": "Principal Investigator · Murata Electronics",
                "points": [
                    "Developed three electrolyte additives that suppress contaminant-metal dendrites on the anode, significantly reducing short-circuit risk.",
                    "Led project design, experimental validation, and implementation with the industry partner.",
                ],
            },
            {
                "title": "Multivalent Energy Storage Development",
                "tag": "Lead Researcher · Singapore NRF",
                "points": [
                    "Invented three magnesium-battery electrolyte systems from commercially available materials.",
                    "Correlated interfacial reactions and Mg-anode surface films with performance.",
                ],
            },
        ],
    },
    {
        "org": "Chungnam National University",
        "place": "Daejeon, Republic of Korea",
        "roles": [("Postdoctoral Fellow", "Sep 2017 – Feb 2018")],
        "projects": [
            {
                "title": "Electrode Structure for Solid-State Polymer Batteries",
                "tag": "",
                "points": [
                    "Built a high-energy all-solid-state battery with a solid polymer electrolyte and NCM811 cathode: 3 mAh/cm² areal capacity with stable cycling.",
                ],
            },
        ],
    },
]

SKILLS = {
    "Materials & electrodes": ["Cathode and anode synthesis", "Solid electrolytes", "Electrolyte formulation",
                               "Slurry electrode coating", "Stack design · N/P ratio"],
    "Cells & electrochemistry": ["Coin and pouch cells", "Three-electrode & in situ cells", "EIS", "CV",
                                 "GITT · PITT", "dQ/dV · dV/dQ"],
    "Characterization": ["XRD", "XPS", "SEM-EDS", "ICP", "BET", "Raman", "ATR-FTIR", "UV-Vis",
                         "Post-mortem analysis"],
    "Data, AI & prototyping": ["AI-assisted data analysis", "AI-assisted experiment design", "Python",
                               "Cloud HPC & ML screening", "SolidWorks", "AutoCAD", "3D printing"],
}

SCHOLAR_URL = LINKS["Google Scholar"]
PDF_FOLDER_URL = LINKS["Paper PDFs"]

# "pdf": paste the Google Drive share link of that paper's PDF; empty = link to the whole folder.
PUBLICATIONS = [
    {"title": "In situ cryogenic X-ray photoelectron spectroscopy unveils metastable components of the solid electrolyte interphase in Li-ion batteries",
     "authors": "Nguyen, D. T., Prabhakaran, V., Shutthanandan, V., Mueller, K. T., Murugesan, V.",
     "venue": "Chem 12(4)", "year": "2026", "url": "https://www.sciencedirect.com/science/article/pii/S2451929425004280", "featured": True, "pdf": ""},
    {"title": "Accelerating computational materials discovery with machine learning and cloud high-performance computing: from large-scale screening to experimental validation",
     "authors": "Chen, C., Nguyen, D. T., et al. (equal contribution)",
     "venue": "J. Am. Chem. Soc.", "year": "2024", "url": "https://pubs.acs.org/doi/10.1021/jacs.4c03849", "featured": False, "pdf": ""},
    {"title": "Structural and chemical evolutions of a magnesium vanadium oxide cathode under electrochemical cycling in magnesium batteries",
     "authors": "Nguyen, D.-T., et al.",
     "venue": "Nano Energy", "year": "2024", "url": "https://www.sciencedirect.com/science/article/pii/S2211285524006888", "featured": False, "pdf": ""},
    {"title": "Stable cycling of Mg metal anodes by regulating the reactivity of Mg²⁺ solvation species",
     "authors": "Li, Z., Nguyen, D.-T., et al. (equal contribution)",
     "venue": "Adv. Energy Mater.", "year": "2024", "url": "https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202301544", "featured": False, "pdf": ""},
    {"title": "Rechargeable magnesium batteries enabled by conventional electrolytes with multifunctional organic chloride additives",
     "authors": "Nguyen, D.-T., Eng, A. Y. S., Horia, R., Sofer, Z., Handoko, A. D., Ng, M.-F., Seh, Z. W.",
     "venue": "Energy Storage Mater.", "year": "2022", "url": "https://www.sciencedirect.com/science/article/pii/S2405829721005274", "featured": False, "pdf": ""},
]

PATENTS = [
    {"title": "Solid-state battery with enhanced solid electrolyte",
     "detail": "US 2026/0142225 A1 · Microsoft Technology Licensing LLC · 2026",
     "url": "https://patents.google.com/patent/US20260142225A1/en", "featured": True, "pdf": ""},
    {"title": "Aluminum-ether-based composition for batteries and ambient temperature aluminum deposition",
     "detail": "U.S. Patent Application 18/130,281", "url": "", "featured": False, "pdf": ""},
    {"title": "An electrolyte for magnesium ion batteries",
     "detail": "U.S. Patent Application 17/780,021", "url": "", "featured": False, "pdf": ""},
    {"title": "Anode active material containing Si composite for lithium secondary batteries",
     "detail": "Republic of Korea Patent 10-1751787 · 2017", "url": "", "featured": False, "pdf": ""},
    {"title": "Anodes for secondary lithium batteries, and preparation method for anode materials",
     "detail": "Republic of Korea Patent 10-1426262 · 2014", "url": "", "featured": False, "pdf": ""},
]

HIGHLIGHTS = [
    # (source, headline, date, url, thumbnail in assets/ or "") - url "" shows the card without a link
    ("Microsoft Source", "Discoveries in weeks, not years: How AI and high-performance computing are speeding up scientific discovery",
     "Jan 9, 2024", "https://news.microsoft.com/source/features/innovation/how-ai-and-hpc-are-speeding-up-scientific-discovery/",
     "hl-microsoft.jpg"),
    ("Fast Company", "Satya Nadella on the bigger vision behind Microsoft's new battery",
     "Jan 9, 2024", "https://www.fastcompany.com/91006385/microsofts-lithium-battery-research-bottle-rocket-azure-quantum-elements",
     "hl-fastcompany.jpg"),
    ("PNNL News", "PNNL research recognized for innovation in grid energy storage",
     "Dec 27, 2024", "https://www.pnnl.gov/news-media/pnnl-research-recognized-innovation-grid-energy-storage", ""),
    ("PNNL · NETS Initiative", "Electrochemical separation and recovery of critical metals (PI)",
     "", "https://www.pnnl.gov/projects/nets/projects", ""),
]

EDUCATION = [
    ("Ph.D., Industrial Chemistry", "Materials development for Li-ion batteries", "Chungnam National University, Republic of Korea", "2017"),
    ("B.S., Chemistry Teacher Education", "", "Quy Nhon University, Vietnam", "2011"),
]
