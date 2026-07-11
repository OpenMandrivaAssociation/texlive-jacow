%global tl_name jacow
%global tl_revision 63060

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.7
Release:	%{tl_revision}.1
Summary:	A class for submissions to the proceedings of conferences on JACoW.org
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jacow
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jacow.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jacow.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The jacow class is used for submissions to the proceedings of
conferences on Joint Accelerator Conferences Website (JACoW), an
international collaboration that publishes the proceedings of
accelerator conferences held around the world.

