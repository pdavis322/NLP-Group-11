function varargout = NLPtool(varargin)

% Run once, then comment out
% matlab.engine.shareEngine;

% NLPTOOL MATLAB code for NLPtool.fig
%      NLPTOOL, by itself, creates a new NLPTOOL or raises the existing
%      singleton*.
%
%      H = NLPTOOL returns the handle to a new NLPTOOL or the handle to
%      the existing singleton*.
%
%      NLPTOOL('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in NLPTOOL.M with the given input arguments.
%
%      NLPTOOL('Property','Value',...) creates a new NLPTOOL or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before NLPtool_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to NLPtool_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help NLPtool

% Last Modified by GUIDE v2.5 10-Apr-2019 16:36:44

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @NLPtool_OpeningFcn, ...
                   'gui_OutputFcn',  @NLPtool_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before NLPtool is made visible.
function NLPtool_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to NLPtool (see VARARGIN)

% Choose default command line output for NLPtool
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes NLPtool wait for user response (see UIRESUME)
% uiwait(handles.figure1);


% --- Outputs from this function are returned to the command line.
function varargout = NLPtool_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;


% --- Executes on selection change in userHash.
function userHash_Callback(hObject, eventdata, handles)
% hObject    handle to userHash (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: contents = cellstr(get(hObject,'String')) returns userHash contents as cell array
%        contents{get(hObject,'Value')} returns selected item from userHash


% --- Executes during object creation, after setting all properties.
function userHash_CreateFcn(hObject, eventdata, handles)
% hObject    handle to userHash (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: popupmenu controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function sourceBox_Callback(hObject, eventdata, handles)
% hObject    handle to sourceBox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of sourceBox as text
%        str2double(get(hObject,'String')) returns contents of sourceBox as a double



% --- Executes during object creation, after setting all properties.
function sourceBox_CreateFcn(hObject, eventdata, handles)
% hObject    handle to sourceBox (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end


% --- Executes on button press in newTweet.
function newTweet_Callback(hObject, eventdata, handles)
% hObject    handle to newTweet (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
NLPtoolF(handles);


% --- Executes on button press in pushTweet.
function pushTweet_Callback(hObject, eventdata, handles)
% hObject    handle to pushTweet (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% py.pushTweet(handles.tweetText.String);
