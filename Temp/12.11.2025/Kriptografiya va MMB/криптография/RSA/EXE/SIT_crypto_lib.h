#pragma once

#ifndef __AFXWIN_H__
#error "include 'stdafx.h' before including this file for PCH"
#endif

#include "resource.h"
class CSIT_crypto_libApp : public CWinApp
{
public:
	CSIT_crypto_libApp();
public:
	virtual BOOL InitInstance();
	DECLARE_MESSAGE_MAP()
};

// Внутренние функции--------------------------------------------------
unsigned __int32 teskari_32(unsigned __int32 son,int fn);
unsigned __int64 teskari_64(unsigned __int32 son,int fn);
unsigned __int32 diter_32(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22);
unsigned __int32 diter4x4_32(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a03,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a13,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22,unsigned __int32 a23,unsigned __int32 a30,unsigned __int32 a31,unsigned __int32 a32,unsigned __int32 a33);
unsigned __int32 diter5x5_32(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a03,unsigned __int32 a04,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a13,unsigned __int32 a14,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22,unsigned __int32 a23,unsigned __int32 a24,unsigned __int32 a30,unsigned __int32 a31,unsigned __int32 a32,unsigned __int32 a33,unsigned __int32 a34,unsigned __int32 a40,unsigned __int32 a41,unsigned __int32 a42,unsigned __int32 a43,unsigned __int32 a44);
unsigned __int32 diter6x6_32(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a03,unsigned __int32 a04,unsigned __int32 a05,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a13,unsigned __int32 a14,unsigned __int32 a15,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22,unsigned __int32 a23,unsigned __int32 a24,unsigned __int32 a25,unsigned __int32 a30,unsigned __int32 a31,unsigned __int32 a32,unsigned __int32 a33,unsigned __int32 a34,unsigned __int32 a35,unsigned __int32 a40,unsigned __int32 a41,unsigned __int32 a42,unsigned __int32 a43,unsigned __int32 a44,unsigned __int32 a45,unsigned __int32 a50,unsigned __int32 a51,unsigned __int32 a52,unsigned __int32 a53,unsigned __int32 a54,unsigned __int32 a55);
unsigned __int32 diter7x7_32(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a03,unsigned __int32 a04,unsigned __int32 a05,unsigned __int32 a06,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a13,unsigned __int32 a14,unsigned __int32 a15,unsigned __int32 a16,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22,unsigned __int32 a23,unsigned __int32 a24,unsigned __int32 a25,unsigned __int32 a26,unsigned __int32 a30,unsigned __int32 a31,unsigned __int32 a32,unsigned __int32 a33,unsigned __int32 a34,unsigned __int32 a35,unsigned __int32 a36,unsigned __int32 a40,unsigned __int32 a41,unsigned __int32 a42,unsigned __int32 a43,unsigned __int32 a44,unsigned __int32 a45,unsigned __int32 a46,unsigned __int32 a50,unsigned __int32 a51,unsigned __int32 a52,unsigned __int32 a53,unsigned __int32 a54,unsigned __int32 a55,unsigned __int32 a56,unsigned __int32 a60,unsigned __int32 a61,unsigned __int32 a62,unsigned __int32 a63,unsigned __int32 a64,unsigned __int32 a65,unsigned __int32 a66);
unsigned __int64 diter_64(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22);
unsigned __int64 diter4x4_64(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a03,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a13,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22,unsigned __int32 a23,unsigned __int32 a30,unsigned __int32 a31,unsigned __int32 a32,unsigned __int32 a33);
unsigned __int64 diter5x5_64(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a03,unsigned __int32 a04,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a13,unsigned __int32 a14,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22,unsigned __int32 a23,unsigned __int32 a24,unsigned __int32 a30,unsigned __int32 a31,unsigned __int32 a32,unsigned __int32 a33,unsigned __int32 a34,unsigned __int32 a40,unsigned __int32 a41,unsigned __int32 a42,unsigned __int32 a43,unsigned __int32 a44);
unsigned __int64 diter6x6_64(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a03,unsigned __int32 a04,unsigned __int32 a05,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a13,unsigned __int32 a14,unsigned __int32 a15,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22,unsigned __int32 a23,unsigned __int32 a24,unsigned __int32 a25,unsigned __int32 a30,unsigned __int32 a31,unsigned __int32 a32,unsigned __int32 a33,unsigned __int32 a34,unsigned __int32 a35,unsigned __int32 a40,unsigned __int32 a41,unsigned __int32 a42,unsigned __int32 a43,unsigned __int32 a44,unsigned __int32 a45,unsigned __int32 a50,unsigned __int32 a51,unsigned __int32 a52,unsigned __int32 a53,unsigned __int32 a54,unsigned __int32 a55);
unsigned __int64 diter7x7_64(unsigned __int32 a00,unsigned __int32 a01,unsigned __int32 a02,unsigned __int32 a03,unsigned __int32 a04,unsigned __int32 a05,unsigned __int32 a06,unsigned __int32 a10,unsigned __int32 a11,unsigned __int32 a12,unsigned __int32 a13,unsigned __int32 a14,unsigned __int32 a15,unsigned __int32 a16,unsigned __int32 a20,unsigned __int32 a21,unsigned __int32 a22,unsigned __int32 a23,unsigned __int32 a24,unsigned __int32 a25,unsigned __int32 a26,unsigned __int32 a30,unsigned __int32 a31,unsigned __int32 a32,unsigned __int32 a33,unsigned __int32 a34,unsigned __int32 a35,unsigned __int32 a36,unsigned __int32 a40,unsigned __int32 a41,unsigned __int32 a42,unsigned __int32 a43,unsigned __int32 a44,unsigned __int32 a45,unsigned __int32 a46,unsigned __int32 a50,unsigned __int32 a51,unsigned __int32 a52,unsigned __int32 a53,unsigned __int32 a54,unsigned __int32 a55,unsigned __int32 a56,unsigned __int32 a60,unsigned __int32 a61,unsigned __int32 a62,unsigned __int32 a63,unsigned __int32 a64,unsigned __int32 a65,unsigned __int32 a66);
unsigned __int32 Imitovstavka_32(unsigned __int8* X);
unsigned __int64 Imitovstavka_64(unsigned __int8* X);
bool Almashtir_32(unsigned __int8* kir);
bool Tes_Almashtir_32(unsigned __int8* kir);
bool Almashtir_64(unsigned __int8* kir);
bool Tes_Almashtir_64(unsigned __int8* kir);
bool SurChapga_32(unsigned __int8* kir);
bool SurChapga_64(unsigned __int8* kir);
bool SurOnga_32(unsigned __int8* kir);
bool SurOnga_64(unsigned __int8* kir);
bool XOR_32(unsigned __int8* a,unsigned __int8* b);
bool XOR_64(unsigned __int8* a,unsigned __int8* b);
bool qoshish_32(unsigned __int32 a,unsigned __int8* b);
bool qoshish_64(unsigned __int64 a,unsigned __int8* b);

//Внешние функции-----------------------------------------------------------
//Функции генерация ключей----------------------------
extern "C" __declspec(dllexport) unsigned __int64 GSCH(void);
extern "C" __declspec(dllexport) unsigned __int8* Gener_keys_32(void);
extern "C" __declspec(dllexport) unsigned __int8* Gener_keys_64(void);
//Функции инициализации----------------------------------
extern "C" __declspec(dllexport) bool Init_umum_par_32(unsigned __int8* umum_par);
extern "C" __declspec(dllexport) bool Init_umum_par_64(unsigned __int8* umum_par);
extern "C" __declspec(dllexport) bool Init_OK_32(unsigned __int8* key_OK);
extern "C" __declspec(dllexport) bool Init_YK_32(unsigned __int8* key_YK);
extern "C" __declspec(dllexport) bool Init_OK_64(unsigned __int8* key_OK);
extern "C" __declspec(dllexport) bool Init_YK_64(unsigned __int8* key_YK);
//Зашифрования-расшифрования одного блока--------------
extern "C" __declspec(dllexport) bool Crypt_blok_base_alg_32(unsigned __int8* pub_blok,unsigned __int8* priv_blok);
extern "C" __declspec(dllexport) bool Decrypt_blok_base_alg_32(unsigned __int8* priv_blok,unsigned __int8* pub_blok);
extern "C" __declspec(dllexport) bool Crypt_blok_base_alg_64(unsigned __int8* pub_blok,unsigned __int8* priv_blok);
extern "C" __declspec(dllexport) bool Decrypt_blok_base_alg_64(unsigned __int8* priv_blok,unsigned __int8* pub_blok);
extern "C" __declspec(dllexport) bool Shakl_S_blok(unsigned __int8* S_qiymat);
extern "C" __declspec(dllexport) bool Tes_Shakl_S_blok(unsigned __int8* S_qiymat);
extern "C" __declspec(dllexport) bool Crypt_blok_iter_alg_32(unsigned __int8* pub_blok,unsigned __int8* priv_blok);
extern "C" __declspec(dllexport) bool Decrypt_blok_iter_alg_32(unsigned __int8* priv_blok,unsigned __int8* pub_blok);
extern "C" __declspec(dllexport) bool Crypt_blok_iter_alg_64(unsigned __int8* pub_blok,unsigned __int8* priv_blok);
extern "C" __declspec(dllexport) bool Decrypt_blok_iter_alg_64(unsigned __int8* priv_blok,unsigned __int8* pub_blok);

// Режимы шифрования---------------------------------------------------------------
// С использованием базового алгоритма-----------------
extern "C" __declspec(dllexport) bool Crypt_rejim_ECB_base_alg_32(unsigned __int8* pub_text,unsigned __int8* prive_text,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_ECB_base_alg_32(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_ECB_base_alg_64(unsigned __int8* pub_text,unsigned __int8* prive_text,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_ECB_base_alg_64(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_CBC_base_alg_32(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int8* IV,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_CBC_base_alg_32(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int8* IV,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_CBC_base_alg_64(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int8* IV,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_CBC_base_alg_64(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int8* IV,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_CTR_base_alg_32(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int8* IV,unsigned __int32 step,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_CTR_base_alg_32(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int8* IV,unsigned __int32 step,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_CTR_base_alg_64(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int8* IV,unsigned __int64 step,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_CTR_base_alg_64(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int8* IV,unsigned __int64 step,unsigned __int64 len);
// С использованием итерационного алгоритма-----------------
extern "C" __declspec(dllexport) bool Crypt_rejim_ECB_iter_alg_32(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_ECB_iter_alg_32(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_ECB_iter_alg_64(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_ECB_iter_alg_64(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_CBC_iter_alg_32(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int8* IV,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_CBC_iter_alg_32(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int8* IV,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_CBC_iter_alg_64(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int8* IV,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_CBC_iter_alg_64(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int8* IV,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_CTR_iter_alg_32(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int8* IV,unsigned __int32 step,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_CTR_iter_alg_32(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int8* IV,unsigned __int32 step,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Crypt_rejim_CTR_iter_alg_64(unsigned __int8* pub_text,unsigned __int8* priv_text,unsigned __int8* IV,unsigned __int64 step,unsigned __int64 len);
extern "C" __declspec(dllexport) bool Decrypt_rejim_CTR_iter_alg_64(unsigned __int8* priv_text,unsigned __int8* pub_text,unsigned __int8* IV,unsigned __int64 step,unsigned __int64 len);
//Функция для очистки памяти------------------------
extern "C" __declspec(dllexport) bool Clear_Mem(void);