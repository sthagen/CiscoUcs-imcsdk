"""This module contains the meta information of ConfigConfMos ExternalMethod."""

from ..imccoremeta import MethodMeta, MethodPropertyMeta

method_meta = MethodMeta("ConfigConfMos", "configConfMos", "Version142b")

prop_meta = {
    "cookie": MethodPropertyMeta("Cookie", "cookie", "StringMin0Max47", "Version142b", "InputOutput", False),
    "in_configs": MethodPropertyMeta("InConfigs", "inConfigs", "ConfigMap", "Version142b", "Input", True),
    "in_hierarchical": MethodPropertyMeta("InHierarchical", "inHierarchical", "Xs:string", "Version142b", "InputOutput", False),
    "out_configs": MethodPropertyMeta("OutConfigs", "outConfigs", "ConfigMap", "Version142b", "Output", True),
}

prop_map = {
    "cookie": "cookie",
    "inConfigs": "in_configs",
    "inHierarchical": "in_hierarchical",
    "outConfigs": "out_configs",
}

