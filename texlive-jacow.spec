Name:		texlive-jacow
Version:	63060
Release:	1
Summary:	A class for submissions to the proceedings of conferences on JACoW.org
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jacow
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jacow.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jacow.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The jacow class is used for submissions to the proceedings of
conferences on Joint Accelerator Conferences Website (JACoW),
an international collaboration that publishes the proceedings
of accelerator conferences held around the world.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/jacow
%doc %{_texmfdistdir}/doc/latex/jacow

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
