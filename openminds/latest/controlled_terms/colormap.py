"""
<description not available>
"""

# this file was auto-generated!

from openminds.base import IRI

from openminds.base import LinkedMetadata
from openminds.properties import Property


class Colormap(LinkedMetadata):
    """
    <description not available>
    """

    type_ = "https://openminds.ebrains.eu/controlledTerms/Colormap"
    context = {"@vocab": "https://openminds.ebrains.eu/vocab/"}
    schema_version = "latest"

    properties = [
        Property(
            "definition",
            str,
            "definition",
            formatting="text/markdown",
            multiline=True,
            description="Short, but precise statement of the meaning of a word, word group, sign or a symbol.",
            instructions="Enter one sentence for defining this term.",
        ),
        Property(
            "description",
            str,
            "description",
            formatting="text/markdown",
            multiline=True,
            description="Longer statement or account giving the characteristics of someone or something.",
            instructions="Enter a short text describing this term.",
        ),
        Property(
            "interlex_identifier",
            IRI,
            "interlexIdentifier",
            description="Persistent identifier for a term registered in the InterLex project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the integrated ontology entry in the InterLex project.",
        ),
        Property(
            "knowledge_space_link",
            IRI,
            "knowledgeSpaceLink",
            description="Persistent link to an encyclopedia entry in the Knowledge Space project.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the wiki page of the corresponding term in the KnowledgeSpace.",
        ),
        Property(
            "name",
            str,
            "name",
            formatting="text/plain",
            required=True,
            description="Word or phrase that constitutes the distinctive designation of a being or thing.",
            instructions="Controlled term originating from a defined terminology.",
        ),
        Property(
            "preferred_ontology_identifier",
            IRI,
            "preferredOntologyIdentifier",
            description="Persistent identifier of a preferred ontological term.",
            instructions="Enter the internationalized resource identifier (IRI) pointing to the preferred ontological term.",
        ),
        Property(
            "synonyms",
            str,
            "synonym",
            multiple=True,
            unique_items=True,
            min_items=1,
            formatting="text/plain",
            description="Words or expressions used in the same language that have the same or nearly the same meaning in some or all senses.",
            instructions="Enter one or several synonyms (including abbreviations) for this controlled term.",
        ),
    ]

    def __init__(
        self,
        id=None,
        definition=None,
        description=None,
        interlex_identifier=None,
        knowledge_space_link=None,
        name=None,
        preferred_ontology_identifier=None,
        synonyms=None,
    ):
        return super().__init__(
            id=id,
            definition=definition,
            description=description,
            interlex_identifier=interlex_identifier,
            knowledge_space_link=knowledge_space_link,
            name=name,
            preferred_ontology_identifier=preferred_ontology_identifier,
            synonyms=synonyms,
        )

    @classmethod
    def instances(cls):
        return [value for value in cls.__dict__.values() if isinstance(value, cls)]

    @classmethod
    def by_name(cls, name):
        if cls._instance_lookup is None:
            cls._instance_lookup = {}
            for instance in cls.instances():
                cls._instance_lookup[instance.name] = instance
                if instance.synonyms:
                    for synonym in instance.synonyms:
                        cls._instance_lookup[synonym] = instance
        return cls._instance_lookup[name]


Colormap.matplotlib_colormaps__accent = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Accent",
    definition="The colormap 'Accent' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Accent",
    synonyms=["Accent"],
)
Colormap.matplotlib_colormaps__blues = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Blues",
    definition="The colormap 'Blues' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Blues",
    synonyms=["Blues"],
)
Colormap.matplotlib_colormaps__br_bg = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.BrBG",
    definition="The colormap 'BrBG' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.BrBG",
    synonyms=["BrBG"],
)
Colormap.matplotlib_colormaps__bu_gn = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.BuGn",
    definition="The colormap 'BuGn' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.BuGn",
    synonyms=["BuGn"],
)
Colormap.matplotlib_colormaps__bu_pu = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.BuPu",
    definition="The colormap 'BuPu' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.BuPu",
    synonyms=["BuPu"],
)
Colormap.matplotlib_colormaps__dark2 = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Dark2",
    definition="The colormap 'Dark2' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Dark2",
    synonyms=["Dark2"],
)
Colormap.matplotlib_colormaps__gn_bu = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.GnBu",
    definition="The colormap 'GnBu' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.GnBu",
    synonyms=["GnBu"],
)
Colormap.matplotlib_colormaps__greens = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Greens",
    definition="The colormap 'Greens' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Greens",
    synonyms=["Greens"],
)
Colormap.matplotlib_colormaps__greys = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Greys",
    definition="The colormap 'Greys' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Greys",
    synonyms=["Greys"],
)
Colormap.matplotlib_colormaps__or_rd = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.OrRd",
    definition="The colormap 'OrRd' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.OrRd",
    synonyms=["OrRd"],
)
Colormap.matplotlib_colormaps__oranges = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Oranges",
    definition="The colormap 'Oranges' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Oranges",
    synonyms=["Oranges"],
)
Colormap.matplotlib_colormaps__paired = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Paired",
    definition="The colormap 'Paired' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Paired",
    synonyms=["Paired"],
)
Colormap.matplotlib_colormaps__pastel1 = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Pastel1",
    definition="The colormap 'Pastel1' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Pastel1",
    synonyms=["Pastel1"],
)
Colormap.matplotlib_colormaps__pastel2 = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Pastel2",
    definition="The colormap 'Pastel2' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Pastel2",
    synonyms=["Pastel2"],
)
Colormap.matplotlib_colormaps__pi_yg = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.PiYG",
    definition="The colormap 'PiYG' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.PiYG",
    synonyms=["PiYG"],
)
Colormap.matplotlib_colormaps__pu_bu = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.PuBu",
    definition="The colormap 'PuBu' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.PuBu",
    synonyms=["PuBu"],
)
Colormap.matplotlib_colormaps__pu_bu_gn = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.PuBuGn",
    definition="The colormap 'PuBuGn' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.PuBuGn",
    synonyms=["PuBuGn"],
)
Colormap.matplotlib_colormaps__pu_or = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.PuOr",
    definition="The colormap 'PuOr' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.PuOr",
    synonyms=["PuOr"],
)
Colormap.matplotlib_colormaps__pu_rd = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.PuRd",
    definition="The colormap 'PuRd' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.PuRd",
    synonyms=["PuRd"],
)
Colormap.matplotlib_colormaps__purples = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Purples",
    definition="The colormap 'Purples' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Purples",
    synonyms=["Purples"],
)
Colormap.matplotlib_colormaps__rd_bu = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.RdBu",
    definition="The colormap 'RdBu' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.RdBu",
    synonyms=["RdBu"],
)
Colormap.matplotlib_colormaps__rd_gy = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.RdGy",
    definition="The colormap 'RdGy' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.RdGy",
    synonyms=["RdGy"],
)
Colormap.matplotlib_colormaps__rd_pu = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.RdPu",
    definition="The colormap 'RdPu' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.RdPu",
    synonyms=["RdPu"],
)
Colormap.matplotlib_colormaps__rd_yl_bu = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.RdYlBu",
    definition="The colormap 'RdYlBu' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.RdYlBu",
    synonyms=["RdYlBu"],
)
Colormap.matplotlib_colormaps__rd_yl_gn = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.RdYlGn",
    definition="The colormap 'RdYlGn' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.RdYlGn",
    synonyms=["RdYlGn"],
)
Colormap.matplotlib_colormaps__reds = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Reds",
    definition="The colormap 'Reds' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Reds",
    synonyms=["Reds"],
)
Colormap.matplotlib_colormaps__set1 = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Set1",
    definition="The colormap 'Set1' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Set1",
    synonyms=["Set1"],
)
Colormap.matplotlib_colormaps__set2 = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Set2",
    definition="The colormap 'Set2' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Set2",
    synonyms=["Set2"],
)
Colormap.matplotlib_colormaps__set3 = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Set3",
    definition="The colormap 'Set3' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Set3",
    synonyms=["Set3"],
)
Colormap.matplotlib_colormaps__spectral = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Spectral",
    definition="The colormap 'Spectral' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Spectral",
    synonyms=["Spectral"],
)
Colormap.matplotlib_colormaps__wistia = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.Wistia",
    definition="The colormap 'Wistia' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.Wistia",
    synonyms=["Wistia"],
)
Colormap.matplotlib_colormaps__yl_gn = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.YlGn",
    definition="The colormap 'YlGn' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.YlGn",
    synonyms=["YlGn"],
)
Colormap.matplotlib_colormaps__yl_gn_bu = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.YlGnBu",
    definition="The colormap 'YlGnBu' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.YlGnBu",
    synonyms=["YlGnBu"],
)
Colormap.matplotlib_colormaps__yl_or_br = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.YlOrBr",
    definition="The colormap 'YlOrBr' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.YlOrBr",
    synonyms=["YlOrBr"],
)
Colormap.matplotlib_colormaps__yl_or_rd = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.YlOrRd",
    definition="The colormap 'YlOrRd' is a sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.YlOrRd",
    synonyms=["YlOrRd"],
)
Colormap.matplotlib_colormaps_afmhot = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.afmhot",
    definition="The colormap 'afmhot' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.afmhot",
    synonyms=["afmhot"],
)
Colormap.matplotlib_colormaps_autumn = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.autumn",
    definition="The colormap 'autumn' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.autumn",
    synonyms=["autumn"],
)
Colormap.matplotlib_colormaps_binary = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.binary",
    definition="The colormap 'binary' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.binary",
    synonyms=["binary"],
)
Colormap.matplotlib_colormaps_bone = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.bone",
    definition="The colormap 'bone' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.bone",
    synonyms=["bone"],
)
Colormap.matplotlib_colormaps_brg = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.brg",
    definition="The colormap 'brg' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.brg",
    synonyms=["brg"],
)
Colormap.matplotlib_colormaps_bwr = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.bwr",
    definition="The colormap 'bwr' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.bwr",
    synonyms=["bwr"],
)
Colormap.matplotlib_colormaps_cividis = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.cividis",
    definition="The colormap 'cividis' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.cividis",
    synonyms=["cividis"],
)
Colormap.matplotlib_colormaps_cm_rmap = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.CMRmap",
    definition="The colormap 'CMRmap' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.CMRmap",
    synonyms=["CMRmap"],
)
Colormap.matplotlib_colormaps_cool = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.cool",
    definition="The colormap 'cool' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.cool",
    synonyms=["cool"],
)
Colormap.matplotlib_colormaps_coolwarm = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.coolwarm",
    definition="The colormap 'coolwarm' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.coolwarm",
    synonyms=["coolwarm"],
)
Colormap.matplotlib_colormaps_copper = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.copper",
    definition="The colormap 'copper' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.copper",
    synonyms=["copper"],
)
Colormap.matplotlib_colormaps_cubehelix = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.cubehelix",
    definition="The colormap 'cubehelix' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.cubehelix",
    synonyms=["cubehelix"],
)
Colormap.matplotlib_colormaps_flag = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.flag",
    definition="The colormap 'flag' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.flag",
    synonyms=["flag"],
)
Colormap.matplotlib_colormaps_gist_earth = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gist_earth",
    definition="The colormap 'gist_earth' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gist_earth",
    synonyms=["gist_earth"],
)
Colormap.matplotlib_colormaps_gist_gray = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gist_gray",
    definition="The colormap 'gist_gray' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gist_gray",
    synonyms=["gist_gray"],
)
Colormap.matplotlib_colormaps_gist_heat = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gist_heat",
    definition="The colormap 'gist_heat' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gist_heat",
    synonyms=["gist_heat"],
)
Colormap.matplotlib_colormaps_gist_ncar = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gist_ncar",
    definition="The colormap 'gist_ncar' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gist_ncar",
    synonyms=["gist_ncar"],
)
Colormap.matplotlib_colormaps_gist_rainbow = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gist_rainbow",
    definition="The colormap 'gist_rainbow' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gist_rainbow",
    synonyms=["gist_rainbow"],
)
Colormap.matplotlib_colormaps_gist_stern = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gist_stern",
    definition="The colormap 'gist_stern' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gist_stern",
    synonyms=["gist_stern"],
)
Colormap.matplotlib_colormaps_gist_yarg = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gist_yarg",
    definition="The colormap 'gist_yarg' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gist_yarg",
    synonyms=["gist_yarg"],
)
Colormap.matplotlib_colormaps_gnuplot = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gnuplot",
    definition="The colormap 'gnuplot' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gnuplot",
    synonyms=["gnuplot"],
)
Colormap.matplotlib_colormaps_gnuplot2 = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gnuplot2",
    definition="The colormap 'gnuplot2' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gnuplot2",
    synonyms=["gnuplot2"],
)
Colormap.matplotlib_colormaps_gray = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.gray",
    definition="The colormap 'gray' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.gray",
    synonyms=["gray"],
)
Colormap.matplotlib_colormaps_hot = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.hot",
    definition="The colormap 'hot' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.hot",
    synonyms=["hot"],
)
Colormap.matplotlib_colormaps_hsv = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.hsv",
    definition="The colormap 'hsv' is a cyclic colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.hsv",
    synonyms=["hsv"],
)
Colormap.matplotlib_colormaps_inferno = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.inferno",
    definition="The colormap 'inferno' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.inferno",
    synonyms=["inferno"],
)
Colormap.matplotlib_colormaps_jet = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.jet",
    definition="The colormap 'jet' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.jet",
    synonyms=["jet"],
)
Colormap.matplotlib_colormaps_magma = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.magma",
    definition="The colormap 'magma' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.magma",
    synonyms=["magma"],
)
Colormap.matplotlib_colormaps_nipy_spectral = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.nipy_spectral",
    definition="The colormap 'nipy_spectral' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.nipy_spectral",
    synonyms=["nipy_spectral"],
)
Colormap.matplotlib_colormaps_ocean = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.ocean",
    definition="The colormap 'ocean' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.ocean",
    synonyms=["ocean"],
)
Colormap.matplotlib_colormaps_pink = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.pink",
    definition="The colormap 'pink' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.pink",
    synonyms=["pink"],
)
Colormap.matplotlib_colormaps_plasma = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.plasma",
    definition="The colormap 'plasma' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.plasma",
    synonyms=["plasma"],
)
Colormap.matplotlib_colormaps_pr_gn = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.PRGn",
    definition="The colormap 'PRGn' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.PRGn",
    synonyms=["PRGn"],
)
Colormap.matplotlib_colormaps_prism = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.prism",
    definition="The colormap 'prism' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.prism",
    synonyms=["prism"],
)
Colormap.matplotlib_colormaps_rainbow = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.rainbow",
    definition="The colormap 'rainbow' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.rainbow",
    synonyms=["rainbow"],
)
Colormap.matplotlib_colormaps_seismic = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.seismic",
    definition="The colormap 'seismic' is a diverging colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.seismic",
    synonyms=["seismic"],
)
Colormap.matplotlib_colormaps_spring = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.spring",
    definition="The colormap 'spring' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.spring",
    synonyms=["spring"],
)
Colormap.matplotlib_colormaps_summer = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.summer",
    definition="The colormap 'summer' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.summer",
    synonyms=["summer"],
)
Colormap.matplotlib_colormaps_tab10 = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.tab10",
    definition="The colormap 'tab10' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.tab10",
    synonyms=["tab10"],
)
Colormap.matplotlib_colormaps_tab20 = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.tab20",
    definition="The colormap 'tab20' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.tab20",
    synonyms=["tab20"],
)
Colormap.matplotlib_colormaps_tab20b = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.tab20b",
    definition="The colormap 'tab20b' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.tab20b",
    synonyms=["tab20b"],
)
Colormap.matplotlib_colormaps_tab20c = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.tab20c",
    definition="The colormap 'tab20c' is a qualitative colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.tab20c",
    synonyms=["tab20c"],
)
Colormap.matplotlib_colormaps_terrain = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.terrain",
    definition="The colormap 'terrain' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.terrain",
    synonyms=["terrain"],
)
Colormap.matplotlib_colormaps_turbo = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.turbo",
    definition="The colormap 'turbo' is a miscellaneous colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.turbo",
    synonyms=["turbo"],
)
Colormap.matplotlib_colormaps_twilight = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.twilight",
    definition="The colormap 'twilight' is a cyclic colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.twilight",
    synonyms=["twilight"],
)
Colormap.matplotlib_colormaps_twilight_shifted = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.twilight_shifted",
    definition="The colormap 'twilight_shifted' is a cyclic colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.twilight_shifted",
    synonyms=["twilight_shifted"],
)
Colormap.matplotlib_colormaps_viridis = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.viridis",
    definition="The colormap 'viridis' is a perceptually uniform sequential colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.viridis",
    synonyms=["viridis"],
)
Colormap.matplotlib_colormaps_winter = Colormap(
    id="https://openminds.ebrains.eu/instances/actionStatusType/matplotlib.colormaps.winter",
    definition="The colormap 'winter' is a sequential (type 2) colormap of the Python plotting library Matplotlib.",
    name="matplotlib.colormaps.winter",
    synonyms=["winter"],
)
