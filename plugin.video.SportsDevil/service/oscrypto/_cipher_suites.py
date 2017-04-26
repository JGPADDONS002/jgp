# coding: utf-8
from __future__ import unicode_literals, division, absolute_import, print_function


__all__ = [
    'CIPHER_SUITE_MAP',
]


CIPHER_SUITE_MAP = {
    b'\x00\x00': 'TLS_NULL_WITH_NULL_NULL',
    b'\x00\x01': 'TLS_RSA_WITH_NULL_MD5',
    b'\x00\x02': 'TLS_RSA_WITH_NULL_SHA',
    b'\x00\x03': 'TLS_RSA_EXPORT_WITH_RC4_40_MD5',
    b'\x00\x04': 'TLS_RSA_WITH_RC4_128_MD5',
    b'\x00\x05': 'TLS_RSA_WITH_RC4_128_SHA',
    b'\x00\x06': 'TLS_RSA_EXPORT_WITH_RC2_CBC_40_MD5',
    b'\x00\x07': 'TLS_RSA_WITH_IDEA_CBC_SHA',
    b'\x00\x08': 'TLS_RSA_EXPORT_WITH_DES40_CBC_SHA',
    b'\x00\x09': 'TLS_RSA_WITH_DES_CBC_SHA',
    b'\x00\x0A': 'TLS_RSA_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x0B': 'TLS_DH_DSS_EXPORT_WITH_DES40_CBC_SHA',
    b'\x00\x0C': 'TLS_DH_DSS_WITH_DES_CBC_SHA',
    b'\x00\x0D': 'TLS_DH_DSS_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x0E': 'TLS_DH_RSA_EXPORT_WITH_DES40_CBC_SHA',
    b'\x00\x0F': 'TLS_DH_RSA_WITH_DES_CBC_SHA',
    b'\x00\x10': 'TLS_DH_RSA_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x11': 'TLS_DHE_DSS_EXPORT_WITH_DES40_CBC_SHA',
    b'\x00\x12': 'TLS_DHE_DSS_WITH_DES_CBC_SHA',
    b'\x00\x13': 'TLS_DHE_DSS_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x14': 'TLS_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA',
    b'\x00\x15': 'TLS_DHE_RSA_WITH_DES_CBC_SHA',
    b'\x00\x16': 'TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x17': 'TLS_DH_anon_EXPORT_WITH_RC4_40_MD5',
    b'\x00\x18': 'TLS_DH_anon_WITH_RC4_128_MD5',
    b'\x00\x19': 'TLS_DH_anon_EXPORT_WITH_DES40_CBC_SHA',
    b'\x00\x1A': 'TLS_DH_anon_WITH_DES_CBC_SHA',
    b'\x00\x1B': 'TLS_DH_anon_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x1E': 'TLS_KRB5_WITH_DES_CBC_SHA',
    b'\x00\x1F': 'TLS_KRB5_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x20': 'TLS_KRB5_WITH_RC4_128_SHA',
    b'\x00\x21': 'TLS_KRB5_WITH_IDEA_CBC_SHA',
    b'\x00\x22': 'TLS_KRB5_WITH_DES_CBC_MD5',
    b'\x00\x23': 'TLS_KRB5_WITH_3DES_EDE_CBC_MD5',
    b'\x00\x24': 'TLS_KRB5_WITH_RC4_128_MD5',
    b'\x00\x25': 'TLS_KRB5_WITH_IDEA_CBC_MD5',
    b'\x00\x26': 'TLS_KRB5_EXPORT_WITH_DES_CBC_40_SHA',
    b'\x00\x27': 'TLS_KRB5_EXPORT_WITH_RC2_CBC_40_SHA',
    b'\x00\x28': 'TLS_KRB5_EXPORT_WITH_RC4_40_SHA',
    b'\x00\x29': 'TLS_KRB5_EXPORT_WITH_DES_CBC_40_MD5',
    b'\x00\x2A': 'TLS_KRB5_EXPORT_WITH_RC2_CBC_40_MD5',
    b'\x00\x2B': 'TLS_KRB5_EXPORT_WITH_RC4_40_MD5',
    b'\x00\x2C': 'TLS_PSK_WITH_NULL_SHA',
    b'\x00\x2D': 'TLS_DHE_PSK_WITH_NULL_SHA',
    b'\x00\x2E': 'TLS_RSA_PSK_WITH_NULL_SHA',
    b'\x00\x2F': 'TLS_RSA_WITH_AES_128_CBC_SHA',
    b'\x00\x30': 'TLS_DH_DSS_WITH_AES_128_CBC_SHA',
    b'\x00\x31': 'TLS_DH_RSA_WITH_AES_128_CBC_SHA',
    b'\x00\x32': 'TLS_DHE_DSS_WITH_AES_128_CBC_SHA',
    b'\x00\x33': 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA',
    b'\x00\x34': 'TLS_DH_anon_WITH_AES_128_CBC_SHA',
    b'\x00\x35': 'TLS_RSA_WITH_AES_256_CBC_SHA',
    b'\x00\x36': 'TLS_DH_DSS_WITH_AES_256_CBC_SHA',
    b'\x00\x37': 'TLS_DH_RSA_WITH_AES_256_CBC_SHA',
    b'\x00\x38': 'TLS_DHE_DSS_WITH_AES_256_CBC_SHA',
    b'\x00\x39': 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA',
    b'\x00\x3A': 'TLS_DH_anon_WITH_AES_256_CBC_SHA',
    b'\x00\x3B': 'TLS_RSA_WITH_NULL_SHA256',
    b'\x00\x3C': 'TLS_RSA_WITH_AES_128_CBC_SHA256',
    b'\x00\x3D': 'TLS_RSA_WITH_AES_256_CBC_SHA256',
    b'\x00\x3E': 'TLS_DH_DSS_WITH_AES_128_CBC_SHA256',
    b'\x00\x3F': 'TLS_DH_RSA_WITH_AES_128_CBC_SHA256',
    b'\x00\x40': 'TLS_DHE_DSS_WITH_AES_128_CBC_SHA256',
    b'\x00\x41': 'TLS_RSA_WITH_CAMELLIA_128_CBC_SHA',
    b'\x00\x42': 'TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA',
    b'\x00\x43': 'TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA',
    b'\x00\x44': 'TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA',
    b'\x00\x45': 'TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA',
    b'\x00\x46': 'TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA',
    b'\x00\x67': 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA256',
    b'\x00\x68': 'TLS_DH_DSS_WITH_AES_256_CBC_SHA256',
    b'\x00\x69': 'TLS_DH_RSA_WITH_AES_256_CBC_SHA256',
    b'\x00\x6A': 'TLS_DHE_DSS_WITH_AES_256_CBC_SHA256',
    b'\x00\x6B': 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA256',
    b'\x00\x6C': 'TLS_DH_anon_WITH_AES_128_CBC_SHA256',
    b'\x00\x6D': 'TLS_DH_anon_WITH_AES_256_CBC_SHA256',
    b'\x00\x84': 'TLS_RSA_WITH_CAMELLIA_256_CBC_SHA',
    b'\x00\x85': 'TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA',
    b'\x00\x86': 'TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA',
    b'\x00\x87': 'TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA',
    b'\x00\x88': 'TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA',
    b'\x00\x89': 'TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA',
    b'\x00\x8A': 'TLS_PSK_WITH_RC4_128_SHA',
    b'\x00\x8B': 'TLS_PSK_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x8C': 'TLS_PSK_WITH_AES_128_CBC_SHA',
    b'\x00\x8D': 'TLS_PSK_WITH_AES_256_CBC_SHA',
    b'\x00\x8E': 'TLS_DHE_PSK_WITH_RC4_128_SHA',
    b'\x00\x8F': 'TLS_DHE_PSK_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x90': 'TLS_DHE_PSK_WITH_AES_128_CBC_SHA',
    b'\x00\x91': 'TLS_DHE_PSK_WITH_AES_256_CBC_SHA',
    b'\x00\x92': 'TLS_RSA_PSK_WITH_RC4_128_SHA',
    b'\x00\x93': 'TLS_RSA_PSK_WITH_3DES_EDE_CBC_SHA',
    b'\x00\x94': 'TLS_RSA_PSK_WITH_AES_128_CBC_SHA',
    b'\x00\x95': 'TLS_RSA_PSK_WITH_AES_256_CBC_SHA',
    b'\x00\x96': 'TLS_RSA_WITH_SEED_CBC_SHA',
    b'\x00\x97': 'TLS_DH_DSS_WITH_SEED_CBC_SHA',
    b'\x00\x98': 'TLS_DH_RSA_WITH_SEED_CBC_SHA',
    b'\x00\x99': 'TLS_DHE_DSS_WITH_SEED_CBC_SHA',
    b'\x00\x9A': 'TLS_DHE_RSA_WITH_SEED_CBC_SHA',
    b'\x00\x9B': 'TLS_DH_anon_WITH_SEED_CBC_SHA',
    b'\x00\x9C': 'TLS_RSA_WITH_AES_128_GCM_SHA256',
    b'\x00\x9D': 'TLS_RSA_WITH_AES_256_GCM_SHA384',
    b'\x00\x9E': 'TLS_DHE_RSA_WITH_AES_128_GCM_SHA256',
    b'\x00\x9F': 'TLS_DHE_RSA_WITH_AES_256_GCM_SHA384',
    b'\x00\xA0': 'TLS_DH_RSA_WITH_AES_128_GCM_SHA256',
    b'\x00\xA1': 'TLS_DH_RSA_WITH_AES_256_GCM_SHA384',
    b'\x00\xA2': 'TLS_DHE_DSS_WITH_AES_128_GCM_SHA256',
    b'\x00\xA3': 'TLS_DHE_DSS_WITH_AES_256_GCM_SHA384',
    b'\x00\xA4': 'TLS_DH_DSS_WITH_AES_128_GCM_SHA256',
    b'\x00\xA5': 'TLS_DH_DSS_WITH_AES_256_GCM_SHA384',
    b'\x00\xA6': 'TLS_DH_anon_WITH_AES_128_GCM_SHA256',
    b'\x00\xA7': 'TLS_DH_anon_WITH_AES_256_GCM_SHA384',
    b'\x00\xA8': 'TLS_PSK_WITH_AES_128_GCM_SHA256',
    b'\x00\xA9': 'TLS_PSK_WITH_AES_256_GCM_SHA384',
    b'\x00\xAA': 'TLS_DHE_PSK_WITH_AES_128_GCM_SHA256',
    b'\x00\xAB': 'TLS_DHE_PSK_WITH_AES_256_GCM_SHA384',
    b'\x00\xAC': 'TLS_RSA_PSK_WITH_AES_128_GCM_SHA256',
    b'\x00\xAD': 'TLS_RSA_PSK_WITH_AES_256_GCM_SHA384',
    b'\x00\xAE': 'TLS_PSK_WITH_AES_128_CBC_SHA256',
    b'\x00\xAF': 'TLS_PSK_WITH_AES_256_CBC_SHA384',
    b'\x00\xB0': 'TLS_PSK_WITH_NULL_SHA256',
    b'\x00\xB1': 'TLS_PSK_WITH_NULL_SHA384',
    b'\x00\xB2': 'TLS_DHE_PSK_WITH_AES_128_CBC_SHA256',
    b'\x00\xB3': 'TLS_DHE_PSK_WITH_AES_256_CBC_SHA384',
    b'\x00\xB4': 'TLS_DHE_PSK_WITH_NULL_SHA256',
    b'\x00\xB5': 'TLS_DHE_PSK_WITH_NULL_SHA384',
    b'\x00\xB6': 'TLS_RSA_PSK_WITH_AES_128_CBC_SHA256',
    b'\x00\xB7': 'TLS_RSA_PSK_WITH_AES_256_CBC_SHA384',
    b'\x00\xB8': 'TLS_RSA_PSK_WITH_NULL_SHA256',
    b'\x00\xB9': 'TLS_RSA_PSK_WITH_NULL_SHA384',
    b'\x00\xBA': 'TLS_RSA_WITH_CAMELLIA_128_CBC_SHA256',
    b'\x00\xBB': 'TLS_DH_DSS_WITH_CAMELLIA_128_CBC_SHA256',
    b'\x00\xBC': 'TLS_DH_RSA_WITH_CAMELLIA_128_CBC_SHA256',
    b'\x00\xBD': 'TLS_DHE_DSS_WITH_CAMELLIA_128_CBC_SHA256',
    b'\x00\xBE': 'TLS_DHE_RSA_WITH_CAMELLIA_128_CBC_SHA256',
    b'\x00\xBF': 'TLS_DH_anon_WITH_CAMELLIA_128_CBC_SHA256',
    b'\x00\xC0': 'TLS_RSA_WITH_CAMELLIA_256_CBC_SHA256',
    b'\x00\xC1': 'TLS_DH_DSS_WITH_CAMELLIA_256_CBC_SHA256',
    b'\x00\xC2': 'TLS_DH_RSA_WITH_CAMELLIA_256_CBC_SHA256',
    b'\x00\xC3': 'TLS_DHE_DSS_WITH_CAMELLIA_256_CBC_SHA256',
    b'\x00\xC4': 'TLS_DHE_RSA_WITH_CAMELLIA_256_CBC_SHA256',
    b'\x00\xC5': 'TLS_DH_anon_WITH_CAMELLIA_256_CBC_SHA256',
    b'\x00\xFF': 'TLS_EMPTY_RENEGOTIATION_INFO_SCSV',
    b'\x13\x01': 'TLS_AES_128_GCM_SHA256',
    b'\x13\x02': 'TLS_AES_256_GCM_SHA384',
    b'\x13\x03': 'TLS_CHACHA20_POLY1305_SHA256',
    b'\x13\x04': 'TLS_AES_128_CCM_SHA256',
    b'\x13\x05': 'TLS_AES_128_CCM_8_SHA256',
    b'\xC0\x01': 'TLS_ECDH_ECDSA_WITH_NULL_SHA',
    b'\xC0\x02': 'TLS_ECDH_ECDSA_WITH_RC4_128_SHA',
    b'\xC0\x03': 'TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA',
    b'\xC0\x04': 'TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA',
    b'\xC0\x05': 'TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA',
    b'\xC0\x06': 'TLS_ECDHE_ECDSA_WITH_NULL_SHA',
    b'\xC0\x07': 'TLS_ECDHE_ECDSA_WITH_RC4_128_SHA',
    b'\xC0\x08': 'TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA',
    b'\xC0\x09': 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA',
    b'\xC0\x0A': 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA',
    b'\xC0\x0B': 'TLS_ECDH_RSA_WITH_NULL_SHA',
    b'\xC0\x0C': 'TLS_ECDH_RSA_WITH_RC4_128_SHA',
    b'\xC0\x0D': 'TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA',
    b'\xC0\x0E': 'TLS_ECDH_RSA_WITH_AES_128_CBC_SHA',
    b'\xC0\x0F': 'TLS_ECDH_RSA_WITH_AES_256_CBC_SHA',
    b'\xC0\x10': 'TLS_ECDHE_RSA_WITH_NULL_SHA',
    b'\xC0\x11': 'TLS_ECDHE_RSA_WITH_RC4_128_SHA',
    b'\xC0\x12': 'TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA',
    b'\xC0\x13': 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA',
    b'\xC0\x14': 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA',
    b'\xC0\x15': 'TLS_ECDH_anon_WITH_NULL_SHA',
    b'\xC0\x16': 'TLS_ECDH_anon_WITH_RC4_128_SHA',
    b'\xC0\x17': 'TLS_ECDH_anon_WITH_3DES_EDE_CBC_SHA',
    b'\xC0\x18': 'TLS_ECDH_anon_WITH_AES_128_CBC_SHA',
    b'\xC0\x19': 'TLS_ECDH_anon_WITH_AES_256_CBC_SHA',
    b'\xC0\x1A': 'TLS_SRP_SHA_WITH_3DES_EDE_CBC_SHA',
    b'\xC0\x1B': 'TLS_SRP_SHA_RSA_WITH_3DES_EDE_CBC_SHA',
    b'\xC0\x1C': 'TLS_SRP_SHA_DSS_WITH_3DES_EDE_CBC_SHA',
    b'\xC0\x1D': 'TLS_SRP_SHA_WITH_AES_128_CBC_SHA',
    b'\xC0\x1E': 'TLS_SRP_SHA_RSA_WITH_AES_128_CBC_SHA',
    b'\xC0\x1F': 'TLS_SRP_SHA_DSS_WITH_AES_128_CBC_SHA',
    b'\xC0\x20': 'TLS_SRP_SHA_WITH_AES_256_CBC_SHA',
    b'\xC0\x21': 'TLS_SRP_SHA_RSA_WITH_AES_256_CBC_SHA',
    b'\xC0\x22': 'TLS_SRP_SHA_DSS_WITH_AES_256_CBC_SHA',
    b'\xC0\x23': 'TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256',
    b'\xC0\x24': 'TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384',
    b'\xC0\x25': 'TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA256',
    b'\xC0\x26': 'TLS_ECDH_ECDSA_WITH_AES_256_CBC_SHA384',
    b'\xC0\x27': 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256',
    b'\xC0\x28': 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384',
    b'\xC0\x29': 'TLS_ECDH_RSA_WITH_AES_128_CBC_SHA256',
    b'\xC0\x2A': 'TLS_ECDH_RSA_WITH_AES_256_CBC_SHA384',
    b'\xC0\x2B': 'TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256',
    b'\xC0\x2C': 'TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384',
    b'\xC0\x2D': 'TLS_ECDH_ECDSA_WITH_AES_128_GCM_SHA256',
    b'\xC0\x2E': 'TLS_ECDH_ECDSA_WITH_AES_256_GCM_SHA384',
    b'\xC0\x2F': 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256',
    b'\xC0\x30': 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384',
    b'\xC0\x31': 'TLS_ECDH_RSA_WITH_AES_128_GCM_SHA256',
    b'\xC0\x32': 'TLS_ECDH_RSA_WITH_AES_256_GCM_SHA384',
    b'\xC0\x33': 'TLS_ECDHE_PSK_WITH_RC4_128_SHA',
    b'\xC0\x34': 'TLS_ECDHE_PSK_WITH_3DES_EDE_CBC_SHA',
    b'\xC0\x35': 'TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA',
    b'\xC0\x36': 'TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA',
    b'\xC0\x37': 'TLS_ECDHE_PSK_WITH_AES_128_CBC_SHA256',
    b'\xC0\x38': 'TLS_ECDHE_PSK_WITH_AES_256_CBC_SHA384',
    b'\xC0\x39': 'TLS_ECDHE_PSK_WITH_NULL_SHA',
    b'\xC0\x3A': 'TLS_ECDHE_PSK_WITH_NULL_SHA256',
    b'\xC0\x3B': 'TLS_ECDHE_PSK_WITH_NULL_SHA384',
    b'\xC0\x3C': 'TLS_RSA_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x3D': 'TLS_RSA_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x3E': 'TLS_DH_DSS_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x3F': 'TLS_DH_DSS_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x40': 'TLS_DH_RSA_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x41': 'TLS_DH_RSA_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x42': 'TLS_DHE_DSS_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x43': 'TLS_DHE_DSS_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x44': 'TLS_DHE_RSA_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x45': 'TLS_DHE_RSA_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x46': 'TLS_DH_anon_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x47': 'TLS_DH_anon_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x48': 'TLS_ECDHE_ECDSA_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x49': 'TLS_ECDHE_ECDSA_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x4A': 'TLS_ECDH_ECDSA_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x4B': 'TLS_ECDH_ECDSA_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x4C': 'TLS_ECDHE_RSA_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x4D': 'TLS_ECDHE_RSA_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x4E': 'TLS_ECDH_RSA_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x4F': 'TLS_ECDH_RSA_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x50': 'TLS_RSA_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x51': 'TLS_RSA_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x52': 'TLS_DHE_RSA_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x53': 'TLS_DHE_RSA_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x54': 'TLS_DH_RSA_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x55': 'TLS_DH_RSA_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x56': 'TLS_DHE_DSS_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x57': 'TLS_DHE_DSS_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x58': 'TLS_DH_DSS_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x59': 'TLS_DH_DSS_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x5A': 'TLS_DH_anon_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x5B': 'TLS_DH_anon_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x5C': 'TLS_ECDHE_ECDSA_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x5D': 'TLS_ECDHE_ECDSA_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x5E': 'TLS_ECDH_ECDSA_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x5F': 'TLS_ECDH_ECDSA_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x60': 'TLS_ECDHE_RSA_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x61': 'TLS_ECDHE_RSA_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x62': 'TLS_ECDH_RSA_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x63': 'TLS_ECDH_RSA_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x64': 'TLS_PSK_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x65': 'TLS_PSK_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x66': 'TLS_DHE_PSK_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x67': 'TLS_DHE_PSK_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x68': 'TLS_RSA_PSK_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x69': 'TLS_RSA_PSK_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x6A': 'TLS_PSK_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x6B': 'TLS_PSK_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x6C': 'TLS_DHE_PSK_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x6D': 'TLS_DHE_PSK_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x6E': 'TLS_RSA_PSK_WITH_ARIA_128_GCM_SHA256',
    b'\xC0\x6F': 'TLS_RSA_PSK_WITH_ARIA_256_GCM_SHA384',
    b'\xC0\x70': 'TLS_ECDHE_PSK_WITH_ARIA_128_CBC_SHA256',
    b'\xC0\x71': 'TLS_ECDHE_PSK_WITH_ARIA_256_CBC_SHA384',
    b'\xC0\x72': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_CBC_SHA256',
    b'\xC0\x73': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_CBC_SHA384',
    b'\xC0\x74': 'TLS_ECDH_ECDSA_WITH_CAMELLIA_128_CBC_SHA256',
    b'\xC0\x75': 'TLS_ECDH_ECDSA_WITH_CAMELLIA_256_CBC_SHA384',
    b'\xC0\x76': 'TLS_ECDHE_RSA_WITH_CAMELLIA_128_CBC_SHA256',
    b'\xC0\x77': 'TLS_ECDHE_RSA_WITH_CAMELLIA_256_CBC_SHA384',
    b'\xC0\x78': 'TLS_ECDH_RSA_WITH_CAMELLIA_128_CBC_SHA256',
    b'\xC0\x79': 'TLS_ECDH_RSA_WITH_CAMELLIA_256_CBC_SHA384',
    b'\xC0\x7A': 'TLS_RSA_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x7B': 'TLS_RSA_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x7C': 'TLS_DHE_RSA_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x7D': 'TLS_DHE_RSA_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x7E': 'TLS_DH_RSA_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x7F': 'TLS_DH_RSA_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x80': 'TLS_DHE_DSS_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x81': 'TLS_DHE_DSS_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x82': 'TLS_DH_DSS_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x83': 'TLS_DH_DSS_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x84': 'TLS_DH_anon_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x85': 'TLS_DH_anon_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x86': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x87': 'TLS_ECDHE_ECDSA_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x88': 'TLS_ECDH_ECDSA_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x89': 'TLS_ECDH_ECDSA_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x8A': 'TLS_ECDHE_RSA_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x8B': 'TLS_ECDHE_RSA_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x8C': 'TLS_ECDH_RSA_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x8D': 'TLS_ECDH_RSA_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x8E': 'TLS_PSK_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x8F': 'TLS_PSK_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x90': 'TLS_DHE_PSK_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x91': 'TLS_DHE_PSK_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x92': 'TLS_RSA_PSK_WITH_CAMELLIA_128_GCM_SHA256',
    b'\xC0\x93': 'TLS_RSA_PSK_WITH_CAMELLIA_256_GCM_SHA384',
    b'\xC0\x94': 'TLS_PSK_WITH_CAMELLIA_128_CBC_SHA256',
    b'\xC0\x95': 'TLS_PSK_WITH_CAMELLIA_256_CBC_SHA384',
    b'\xC0\x96': 'TLS_DHE_PSK_WITH_CAMELLIA_128_CBC_SHA256',
    b'\xC0\x97': 'TLS_DHE_PSK_WITH_CAMELLIA_256_CBC_SHA384',
    b'\xC0\x98': 'TLS_RSA_PSK_WITH_CAMELLIA_128_CBC_SHA256',
    b'\xC0\x99': 'TLS_RSA_PSK_WITH_CAMELLIA_256_CBC_SHA384',
    b'\xC0\x9A': 'TLS_ECDHE_PSK_WITH_CAMELLIA_128_CBC_SHA256',
    b'\xC0\x9B': 'TLS_ECDHE_PSK_WITH_CAMELLIA_256_CBC_SHA384',
    b'\xC0\x9C': 'TLS_RSA_WITH_AES_128_CCM',
    b'\xC0\x9D': 'TLS_RSA_WITH_AES_256_CCM',
    b'\xC0\x9E': 'TLS_DHE_RSA_WITH_AES_128_CCM',
    b'\xC0\x9F': 'TLS_DHE_RSA_WITH_AES_256_CCM',
    b'\xC0\xA0': 'TLS_RSA_WITH_AES_128_CCM_8',
    b'\xC0\xA1': 'TLS_RSA_WITH_AES_256_CCM_8',
    b'\xC0\xA2': 'TLS_DHE_RSA_WITH_AES_128_CCM_8',
    b'\xC0\xA3': 'TLS_DHE_RSA_WITH_AES_256_CCM_8',
    b'\xC0\xA4': 'TLS_PSK_WITH_AES_128_CCM',
    b'\xC0\xA5': 'TLS_PSK_WITH_AES_256_CCM',
    b'\xC0\xA6': 'TLS_DHE_PSK_WITH_AES_128_CCM',
    b'\xC0\xA7': 'TLS_DHE_PSK_WITH_AES_256_CCM',
    b'\xC0\xA8': 'TLS_PSK_WITH_AES_128_CCM_8',
    b'\xC0\xA9': 'TLS_PSK_WITH_AES_256_CCM_8',
    b'\xC0\xAA': 'TLS_PSK_DHE_WITH_AES_128_CCM_8',
    b'\xC0\xAB': 'TLS_PSK_DHE_WITH_AES_256_CCM_8',
    b'\xCC\xA8': 'TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256',
    b'\xCC\xA9': 'TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256',
    b'\xCC\xAA': 'TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256',
    b'\xCC\xAB': 'TLS_PSK_WITH_CHACHA20_POLY1305_SHA256',
    b'\xCC\xAC': 'TLS_ECDHE_PSK_WITH_CHACHA20_POLY1305_SHA256',
    b'\xCC\xAD': 'TLS_DHE_PSK_WITH_CHACHA20_POLY1305_SHA256',
    b'\xCC\xAE': 'TLS_RSA_PSK_WITH_CHACHA20_POLY1305_SHA256',
}
