// VijinerDlg.cpp : implementation file
//

#include "stdafx.h"
#include "Vijiner.h"
#include "VijinerDlg.h"
#include ".\vijinerdlg.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CAboutDlg dialog used for App About

class CAboutDlg : public CDialog
{
public:
	CAboutDlg();

// Dialog Data
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV support

// Implementation
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialog(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialog)
END_MESSAGE_MAP()


// CVijinerDlg dialog



CVijinerDlg::CVijinerDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CVijinerDlg::IDD, pParent)
	, key_file(_T(""))
	, pub_text(_T(""))
	, priv_text(_T(""))

{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CVijinerDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	DDX_Text(pDX, IDC_EDIT1, key_file);
	DDX_Text(pDX, IDC_EDIT2, pub_text);
	DDX_Text(pDX, IDC_EDIT3, priv_text);
	
}

BEGIN_MESSAGE_MAP(CVijinerDlg, CDialog)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	//}}AFX_MSG_MAP
	ON_BN_CLICKED(IDC_BUTTON1, OnBnClickedButton1)
	ON_BN_CLICKED(IDC_BUTTON2, OnBnClickedButton2)
	ON_BN_CLICKED(IDC_BUTTON3, OnBnClickedButton3)
	ON_BN_CLICKED(IDC_BUTTON4, OnBnClickedButton4)
	ON_BN_CLICKED(IDC_BUTTON5, OnBnClickedButton5)
	ON_BN_CLICKED(IDC_BUTTON6, OnBnClickedButton6)
END_MESSAGE_MAP()


// CVijinerDlg message handlers

BOOL CVijinerDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// Add "About..." menu item to system menu.

	// IDM_ABOUTBOX must be in the system command range.
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		CString strAboutMenu;
		strAboutMenu.LoadString(IDS_ABOUTBOX);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// Set the icon for this dialog.  The framework does this automatically
	//  when the application's main window is not a dialog
	SetIcon(m_hIcon, TRUE);			// Set big icon
	SetIcon(m_hIcon, FALSE);		// Set small icon

	// TODO: Add extra initialization here
	
	return TRUE;  // return TRUE  unless you set the focus to a control
}

void CVijinerDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// If you add a minimize button to your dialog, you will need the code below
//  to draw the icon.  For MFC applications using the document/view model,
//  this is automatically done for you by the framework.

void CVijinerDlg::OnPaint() 
{
	if (IsIconic())
	{
		CPaintDC dc(this); // device context for painting

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// Center icon in client rectangle
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// Draw the icon
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// The system calls this function to obtain the cursor to display while the user drags
//  the minimized window.
HCURSOR CVijinerDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

void CVijinerDlg::OnBnClickedButton1()
{
    UpdateData(TRUE);
	CFileDialog dlg(FALSE);
	if(dlg.DoModal()==IDOK)
	{
		srand((unsigned int)time(NULL));
		key_file=dlg.GetPathName();
		char c[1],a[256],b[256];
www:	c[0]=rand()%256;
		if(c[0]==0) goto www;
		int i,j;
        for(i=0;i<256;i++)
		{
wer:        a[i]=rand()%256;
			for(j=0;j<i;j++)
				if(a[i]==b[j]) goto wer;
			b[i]=a[i];
		}
		CFile file;
		file.Open(key_file,CFile::modeCreate| CFile::modeWrite);
        file.Write(c,1);
		file.Write(a,256);
		file.Close();
	}
	UpdateData(FALSE);
}

void CVijinerDlg::OnBnClickedButton2()
{
	UpdateData(TRUE);
	CFileDialog dlg(TRUE);
	if(dlg.DoModal()==IDOK)
	{
		key_file=dlg.GetPathName();
		UpdateData(FALSE);
	}
}

void CVijinerDlg::OnBnClickedButton3()
{
	UpdateData(TRUE);
	CFileDialog dlg(TRUE);
	if(dlg.DoModal()==IDOK)
	{
		pub_text=dlg.GetPathName();
		UpdateData(FALSE);
	}
}

void CVijinerDlg::OnBnClickedButton4()
{
	UpdateData(TRUE);
	CFileDialog dlg(TRUE);
	if(dlg.DoModal()==IDOK)
	{
		priv_text=dlg.GetPathName();
		UpdateData(FALSE);
	}
}

void CVijinerDlg::OnBnClickedButton5()
{
	CFile file;
	file.Open(key_file,CFile::modeRead);
	char c[1],key[256];
	file.Read(c,1);
	file.Read(key,256);
	file.Close();
	file.Open(pub_text,CFile::modeRead);
	unsigned int fsize=file.GetLength();
	char *belgi,*shbelgi;
	belgi=new char[fsize];
	shbelgi=new char[fsize];
	file.Read(belgi,fsize);
	file.Close();
	unsigned int i;
	for(i=0;i<fsize;i++)
	{
	  if(i==0) 
	   	   shbelgi[0]=key[((belgi[0]+256)%256+(c[0]+256)%256)%256];
	  else
	       shbelgi[i]=key[((belgi[i]+256)%256+(belgi[i-1]+256)%256)%256];
	}
	file.Open(priv_text,CFile::modeCreate| CFile::modeWrite);
	file.Write(shbelgi,fsize);
	file.Close();
	delete [] belgi;
	delete [] shbelgi;
	MessageBox("Crypt Finished ...");
}

void CVijinerDlg::OnBnClickedButton6()
{
	CFile file;
	file.Open(key_file,CFile::modeRead);
	char c[1],key[256];
	file.Read(c,1);
	file.Read(key,256);
	file.Close();
	file.Open(priv_text,CFile::modeRead);
	unsigned int fsize=file.GetLength();
	char *belgi,*shbelgi;
	belgi=new char[fsize];
	shbelgi=new char[fsize];
	file.Read(shbelgi,fsize);
	file.Close();
	unsigned int i;
	for(i=0;i<fsize;i++)
	{
		int k;
	   for(k=0;k<256;k++)
		   if((shbelgi[i]+256)%256==(key[k]+256)%256) break;
	   
	   if(i==0) 
	   	   belgi[0]=(k-(c[0]+256)%256+256)%256;
	   else
           belgi[i]=(k-(belgi[i-1]+256)%256+256)%256;
	}
	file.Open(pub_text,CFile::modeCreate| CFile::modeWrite);
	file.Write(belgi,fsize);
	file.Close();
	delete [] belgi;
	delete [] shbelgi;
	MessageBox("Decrypt Finished ...");
}
