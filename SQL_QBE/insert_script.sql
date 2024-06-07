
 

--CREATE TABLE [PricingRaterDropdownData](

--       [DropdownID] [int] IDENTITY(1,1) primary key,

--       [RaterType] [varchar](50) NOT NULL,

--       [DropDownSection] [varchar](100) NULL,

--       [DropdownControlId] [varchar](100) NOT NULL,

--       [DropdownValue] [varchar](500) NOT NULL,

--       [DropdownText] [varchar](2000) NOT NULL,

--       [DropdownStatus] [varchar](50) NOT NULL,
--)


INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type1', 'Section1', 'Control1', 'Value1', 'Text1', 'Status1');
INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type2', 'Section2', 'Control2', 'Value2', 'Text2', 'Status2');
INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type3', 'Section3', 'Control3', 'Value3', 'Text3', 'Status3');
INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type4', 'Section4', 'Control4', 'Value4', 'Text4', 'Status4');
INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type5', 'Section5', 'Control5', 'Value5', 'Text5', 'Status5');
INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type6', 'Section6', 'Control6', 'Value6', 'Text6', 'Status6');
INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type7', 'Section7', 'Control7', 'Value7', 'Text7', 'Status7');
INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type8', 'Section8', 'Control8', 'Value8', 'Text8', 'Status8');
INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type9', 'Section9', 'Control9', 'Value9', 'Text9', 'Status9');
INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES ('Type10', 'Section10', 'Control10', 'Value10', 'Text10', 'Status10');

select * from [PricingRaterDropdownData];



DECLARE @InsertStatement NVARCHAR(MAX) = '';

SELECT @InsertStatement = @InsertStatement + 'INSERT INTO [PricingRaterDropdownData] (RaterType, DropDownSection, DropdownControlId, DropdownValue, DropdownText, DropdownStatus) VALUES (''' 
    + RaterType + ''', ''' 
    + ISNULL(DropDownSection, '') + ''', ''' 
    + DropdownControlId + ''', ''' 
    + DropdownValue + ''', ''' 
    + DropdownText + ''', ''' 
    + DropdownStatus + ''');' + CHAR(13) + CHAR(10)
FROM [PricingRaterDropdownData];

PRINT @InsertStatement;

 

