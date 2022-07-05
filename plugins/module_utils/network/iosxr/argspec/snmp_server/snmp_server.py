# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the
# cli_rm_builder.
#
# Manually editing this file is not advised.
#
# To update the argspec make the desired changes
# in the module docstring and re-run
# cli_rm_builder.
#
#############################################

"""
The arg spec for the iosxr_snmp_server module
"""


class Snmp_serverArgs(object):  # pylint: disable=R0903
    """The arg spec for the iosxr_snmp_server module"""

    argument_spec = {
        "config": {
            "type": "dict",
            "options": {
                "chassis_id": {"type": "str"},
                "communities": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "acl_v4": {"type": "str"},
                        "acl_v6": {"type": "str"},
                        "ro": {"type": "bool"},
                        "rw": {"type": "bool"},
                        "sdrowner": {"type": "bool"},
                        "systemowner": {"type": "bool"},
                        "v4_acl": {"type": "str"},
                    },
                },
                "community_maps": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "context": {"type": "str"},
                        "security_name": {"type": "str"},
                        "target_list": {"type": "str"},
                    },
                },
                "correlator": {
                    "type": "dict",
                    "options": {
                        "buffer_size": {"type": "int"},
                        "rules": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "rule_name": {"type": "str"},
                                "timeout": {"type": "int"},
                            },
                        },
                        "rule_sets": {
                            "type": "list",
                            "elements": "dict",
                            "options": {"name": {"type": "str"}},
                        },
                    },
                },
                "contact": {"type": "str"},
                "context": {"type": "list", "elements": "str"},
                "drop": {
                    "type": "dict",
                    "options": {
                        "unknown_user": {"type": "bool"},
                        "report_IPv4": {"type": "str"},
                        "report_IPv6": {"type": "str"},
                    },
                },
                "engineid": {
                    "type": "dict",
                    "options": {"local": {"type": "str"}},
                },
                "groups": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "group": {"type": "str"},
                        "version": {
                            "type": "str",
                            "choices": ["v1", "v3", "v2c"],
                        },
                        "context": {"type": "str"},
                        "notify": {"type": "str"},
                        "read": {"type": "str"},
                        "write": {"type": "str"},
                        "acl_v4": {"type": "str", "aliases": ["Ipv4_acl"]},
                        "acl_v6": {"type": "str", "aliases": ["Ipv6_acl"]},
                        "v4_acl": {"type": "str"},
                    },
                },
                "hosts": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "host": {"type": "str"},
                        "community": {"type": "str"},
                        "udp_port": {"type": "int"},
                        "informs": {"type": "bool"},
                        "traps": {"type": "bool"},
                        "version": {
                            "type": "str",
                            "choices": ["1", "2c", "3"],
                        },
                    },
                },
                "ifindex": {"type": "bool"},
                "ifmib": {
                    "type": "dict",
                    "options": {
                        "ifalias_long": {"type": "bool"},
                        "internal_cache_max_duration": {"type": "int"},
                        "ipsubscriber": {"type": "bool"},
                        "stats": {"type": "bool"},
                    },
                },
                "inform": {
                    "options": {
                        "pending": {"type": "int"},
                        "retries": {"type": "int"},
                        "timeout": {"type": "int"},
                    },
                    "type": "dict",
                },
                "interfaces": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "notification_linkupdown_disable": {"type": "bool"},
                        "index_persistent": {"type": "bool"},
                    },
                },
                "ipv4": {
                    "type": "dict",
                    "options": {
                        "dscp": {"type": "str"},
                        "precedence": {"type": "str"},
                    },
                },
                "ipv6": {
                    "type": "dict",
                    "options": {
                        "dscp": {"type": "str"},
                        "precedence": {"type": "str"},
                    },
                },
                "location": {"type": "str"},
                "logging_threshold_oid_processing": {"type": "int"},
                "logging_threshold_pdu_processing": {"type": "int"},
                "mib_bulkstat_max_procmem_size": {"type": "int"},
                "mib_object_lists": {"type": "list", "elements": "str"},
                "mib_schema": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "object_list": {"type": "str"},
                        "poll_interval": {"type": "int"},
                    },
                },
                "mib_bulkstat_transfer_ids": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "buffer_size": {"type": "int"},
                        "enable": {"type": "bool"},
                        "format_schemaASCI": {"type": "bool"},
                        "retain": {"type": "int"},
                        "retry": {"type": "int"},
                        "schema": {"type": "str"},
                        "transfer_interval": {"type": "int"},
                    },
                },
                "mroutemib_send_all_vrf": {"type": "bool"},
                "notification_log_mib": {
                    "type": "dict",
                    "options": {
                        "GlobalSize": {"type": "int"},
                        "default": {"type": "bool"},
                        "disable": {"type": "bool"},
                        "size": {"type": "int"},
                    },
                },
                "oid_poll_stats": {"type": "bool"},
                "overload_control": {
                    "type": "dict",
                    "options": {
                        "overload_drop_time": {"type": "int"},
                        "overload_throttle_rate": {"type": "int"},
                    },
                },
                "packetsize": {"type": "int"},
                "queue_length": {"type": "int"},
                "targets": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "name": {"type": "str"},
                        "host": {"type": "str"},
                        "vrf": {"type": "str"},
                    },
                },
                "throttle_time": {"type": "int"},
                "timeouts": {
                    "type": "dict",
                    "options": {
                        "duplicate": {"type": "int"},
                        "inQdrop": {"type": "int"},
                        "pdu_stats": {"type": "int"},
                        "subagent": {"type": "int"},
                        "threshold": {"type": "int"},
                    },
                },
                "trap": {
                    "type": "dict",
                    "options": {
                        "authentication_vrf_disable": {"type": "bool"},
                        "link_ietf": {"type": "bool"},
                        "throttle_time": {"type": "int"},
                    },
                },
                "trap_source": {"type": "str"},
                "trap_timeout": {"type": "int"},
                "traps": {
                    "type": "dict",
                    "options": {
                        "addrpool": {
                            "type": "dict",
                            "options": {
                                "low": {"type": "bool"},
                                "high": {"type": "bool"},
                            },
                        },
                        "bfd": {"type": "bool"},
                        "bgp": {
                            "type": "dict",
                            "options": {
                                "cbgp2": {"type": "bool"},
                                "updown": {"type": "bool"},
                            },
                        },
                        "bulkstat_collection": {"type": "bool"},
                        "bulkstat_transfer": {"type": "bool"},
                        "bridgemib": {"type": "bool"},
                        "copy_complete": {"type": "bool"},
                        "cisco_entity_ext": {"type": "bool"},
                        "config": {"type": "bool"},
                        "diameter": {
                            "type": "dict",
                            "options": {
                                "peerdown": {"type": "bool"},
                                "peerup": {"type": "bool"},
                                "permanentfail": {"type": "bool"},
                                "protocolerror": {"type": "bool"},
                                "transientfail": {"type": "bool"},
                            },
                        },
                        "entity": {"type": "bool"},
                        "entity_redundancy": {
                            "type": "dict",
                            "options": {
                                "all": {"type": "bool"},
                                "status": {"type": "bool"},
                                "switchover": {"type": "bool"},
                            },
                        },
                        "entity_state": {
                            "type": "dict",
                            "options": {
                                "operstatus": {"type": "bool"},
                                "switchover": {"type": "bool"},
                            },
                        },
                        "flash": {
                            "type": "dict",
                            "options": {
                                "insertion": {"type": "bool"},
                                "removal": {"type": "bool"},
                            },
                        },
                        "fru_ctrl": {"type": "bool"},
                        "hsrp": {"type": "bool"},
                        "ipsla": {"type": "bool"},
                        "ipsec": {
                            "type": "dict",
                            "options": {
                                "start": {"type": "bool"},
                                "stop": {"type": "bool"},
                            },
                        },
                        "isakmp": {
                            "type": "dict",
                            "options": {
                                "start": {"type": "bool"},
                                "stop": {"type": "bool"},
                            },
                        },
                        "isis": {
                            "type": "dict",
                            "options": {
                                "adjacency_change": {"type": "bool"},
                                "all": {"type": "bool"},
                                "area_mismatch": {"type": "bool"},
                                "attempt_to_exceed_max_sequence": {
                                    "type": "bool"
                                },
                                "authentication_failure": {"type": "bool"},
                                "authentication_type_failure": {
                                    "type": "bool"
                                },
                                "corrupted_lsp_detected": {"type": "bool"},
                                "database_overload": {"type": "bool"},
                                "id_len_mismatch": {"type": "bool"},
                                "lsp_error_detected": {"type": "bool"},
                                "lsp_too_large_to_propagate": {"type": "bool"},
                                "manual_address_drops": {"type": "bool"},
                                "max_area_addresses_mismatch": {
                                    "type": "bool"
                                },
                                "orig_lsp_buff_size_mismatch": {
                                    "type": "bool"
                                },
                                "version_skew": {"type": "bool"},
                                "own_lsp_purge": {"type": "bool"},
                                "rejected_adjacency": {"type": "bool"},
                                "protocols_supported_mismatch": {
                                    "type": "bool"
                                },
                                "sequence_number_skip": {"type": "bool"},
                            },
                        },
                        "l2tun": {
                            "type": "dict",
                            "options": {
                                "pseudowire_status": {"type": "bool"},
                                "sessions": {"type": "bool"},
                                "tunnel_down": {"type": "bool"},
                                "tunnel_up": {"type": "bool"},
                            },
                        },
                        "l2vpn": {
                            "type": "dict",
                            "options": {
                                "all": {"type": "bool"},
                                "cisco": {"type": "bool"},
                                "vc_down": {"type": "bool"},
                                "vc_up": {"type": "bool"},
                            },
                        },
                        "msdp_peer_state_change": {"type": "bool"},
                        "ntp": {"type": "bool"},
                        "ospf": {
                            "type": "dict",
                            "options": {
                                "errors": {
                                    "type": "dict",
                                    "options": {
                                        "bad_packet": {"type": "bool"},
                                        "authentication_failure": {
                                            "type": "bool"
                                        },
                                        "config_error": {"type": "bool"},
                                        "virt_bad_packet": {"type": "bool"},
                                        "virt_authentication_failure": {
                                            "type": "bool"
                                        },
                                        "virt_config_error": {"type": "bool"},
                                    },
                                },
                                "lsa": {
                                    "type": "dict",
                                    "options": {
                                        "lsa_maxage": {"type": "bool"},
                                        "lsa_originate": {"type": "bool"},
                                    },
                                },
                                "retransmit": {
                                    "type": "dict",
                                    "options": {
                                        "packets": {"type": "bool"},
                                        "virt_packets": {"type": "bool"},
                                    },
                                },
                                "state_change": {
                                    "type": "dict",
                                    "options": {
                                        "if_state_change": {"type": "bool"},
                                        "neighbor_state_change": {
                                            "type": "bool"
                                        },
                                        "virtif_state_change": {
                                            "type": "bool"
                                        },
                                        "virtneighbor_state_change": {
                                            "type": "bool"
                                        },
                                    },
                                },
                            },
                        },
                        "ospfv3": {
                            "type": "dict",
                            "options": {
                                "errors": {
                                    "type": "dict",
                                    "options": {
                                        "bad_packet": {"type": "bool"},
                                        "config_error": {"type": "bool"},
                                        "virt_bad_packet": {"type": "bool"},
                                        "virt_config_error": {"type": "bool"},
                                    },
                                },
                                "state_change": {
                                    "type": "dict",
                                    "options": {
                                        "if_state_change": {"type": "bool"},
                                        "neighbor_state_change": {
                                            "type": "bool"
                                        },
                                        "virtif_state_change": {
                                            "type": "bool"
                                        },
                                        "virtneighbor_state_change": {
                                            "type": "bool"
                                        },
                                        "nssa_state_change": {"type": "bool"},
                                        "restart_status_change": {
                                            "type": "bool"
                                        },
                                        "restart_helper_status_change": {
                                            "type": "bool"
                                        },
                                        "restart_virtual_helper_status_change": {
                                            "type": "bool"
                                        },
                                    },
                                },
                            },
                        },
                        "power": {"type": "bool"},
                        "rf": {"type": "bool"},
                        "pim": {
                            "type": "dict",
                            "options": {
                                "interface_state_change": {"type": "bool"},
                                "invalid_message_received": {"type": "bool"},
                                "neighbor_change": {"type": "bool"},
                                "rp_mapping_change": {"type": "bool"},
                            },
                        },
                        "rsvp": {
                            "type": "dict",
                            "options": {
                                "all": {"type": "bool"},
                                "lost_flow": {"type": "bool"},
                                "new_flow": {"type": "bool"},
                            },
                        },
                        "selective_vrf_download_role_change": {"type": "bool"},
                        "sensor": {"type": "bool"},
                        "snmp": {
                            "type": "dict",
                            "options": {
                                "authentication": {"type": "bool"},
                                "linkdown": {"type": "bool"},
                                "linkup": {"type": "bool"},
                                "warmstart": {"type": "bool"},
                                "coldstart": {"type": "bool"},
                            },
                        },
                        "vrrp_events": {"type": "bool"},
                        "syslog": {"type": "bool"},
                        "subscriber": {
                            "type": "dict",
                            "options": {
                                "session_agg_access_interface": {
                                    "type": "bool"
                                },
                                "session_agg_node": {"type": "bool"},
                            },
                        },
                        "system": {"type": "bool"},
                        "vpls": {
                            "type": "dict",
                            "options": {
                                "all": {"type": "bool"},
                                "full_clear": {"type": "bool"},
                                "full_raise": {"type": "bool"},
                                "status": {"type": "bool"},
                            },
                        },
                    },
                },
                "users": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "user": {"type": "str"},
                        "group": {"type": "str"},
                        "acl_v4": {"type": "str", "aliases": ["Ipv4_acl"]},
                        "acl_v6": {"type": "str", "aliases": ["Ipv6_acl"]},
                        "SDROwner": {"type": "bool"},
                        "SystemOwner": {"type": "bool"},
                        "v4_acl": {"type": "str"},
                        "version": {
                            "type": "str",
                            "choices": ["v1", "v2c", "v3"],
                        },
                    },
                },
                "vrfs": {
                    "type": "list",
                    "elements": "dict",
                    "options": {
                        "vrf": {"type": "str"},
                        "context": {"type": "list", "elements": "str"},
                        "hosts": {
                            "type": "list",
                            "elements": "dict",
                            "options": {
                                "host": {"type": "str"},
                                "community": {"type": "str"},
                                "udp_port": {"type": "int"},
                                "informs": {"type": "bool"},
                                "traps": {"type": "bool"},
                                "version": {
                                    "type": "str",
                                    "choices": ["1", "2c", "3"],
                                },
                            },
                        },
                    },
                },
            },
        },
        "running_config": {"type": "str"},
        "state": {
            "type": "str",
            "choices": [
                "deleted",
                "merged",
                "overridden",
                "replaced",
                "gathered",
                "rendered",
                "parsed",
            ],
            "default": "merged",
        },
    }  # pylint: disable=C0301