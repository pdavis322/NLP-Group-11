%% NLPtoolF.m
%  This will be the program that collects data from the GUI and
%  communicates to Python then takes data from Python and communicates to
%  the GUI

function NLPtoolF(handles)

%% Collect the necessary data

% baseSource=handles.userHash.Value;
 desSource=handles.sourceHash.String;

% Call the Python function that's going to get tweets. Should look
% something like:

% tweetArray={py.getName(1, desSource)};

% This will get an array of strings

% Then we will call the matlab function that will build the dictionary,
% tokenize, then generate the string

% tweetString=py.genTweet(rawArray);

handles.tweetText.String=tweetString;


