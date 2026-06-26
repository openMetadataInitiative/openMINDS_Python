# this file was auto-generated!


from openminds.v4.controlled_terms.product_accessibility import ProductAccessibility


ProductAccessibility.controlled_access = ProductAccessibility(
    id="https://openminds.om-i.org/instances/productAccessibility/controlledAccess",
    definition="With 'controlled access' selected, data and metadata are both released and available free of charge, but users must logged in and authenticated themselves to access the data.",
    name="controlled access",
)

ProductAccessibility.free_access = ProductAccessibility(
    id="https://openminds.om-i.org/instances/productAccessibility/freeAccess",
    definition="With 'free access' selected, data and metadata are both released and become immediately available without any access restrictions.",
    name="free access",
)

ProductAccessibility.paid_access = ProductAccessibility(
    id="https://openminds.om-i.org/instances/productAccessibility/paidAccess",
    definition="With 'paid access' selected, data and metadata are both released, but users paid to gain access to the data (e.g., a one-time fee).",
    name="paid access",
)

ProductAccessibility.restricted_access = ProductAccessibility(
    id="https://openminds.om-i.org/instances/productAccessibility/restrictedAccess",
    definition="With 'restricted access' selected, metadata are released, but data remain on an access restricted server.",
    name="restricted access",
)

ProductAccessibility.retracted = ProductAccessibility(
    id="https://openminds.om-i.org/instances/productAccessibility/retracted",
    definition="With 'retracted' selected, metadata are released, but data are retracted.",
    name="retracted",
)

ProductAccessibility.under_embargo = ProductAccessibility(
    id="https://openminds.om-i.org/instances/productAccessibility/underEmbargo",
    definition="With 'under embargo' selected, metadata are released, but data remain unavailable for the public until the embargo is lifted.",
    name="under embargo",
)
