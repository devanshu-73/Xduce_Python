CREATE TABLE ExampleTable (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Column1 VARCHAR(50),
    Column2 VARCHAR(50),
    Column3 VARCHAR(50),
    Column4 VARCHAR(50),
    Column5 VARCHAR(50),
    Column6 VARCHAR(50),
    Column7 VARCHAR(50),
    Column8 VARCHAR(50),
    Column9 VARCHAR(50),
    Column10 VARCHAR(50)
);

-- Insert data into the table
INSERT INTO ExampleTable (Column1, Column2, Column3, Column4, Column5, Column6, Column7, Column8, Column9, Column10)
VALUES
    ('Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10'),
    ('Data11', 'Data12', 'Data13', 'Data14', 'Data15', 'Data16', 'Data17', 'Data18', 'Data19', 'Data20'),
    ('Data21', 'Data22', 'Data23', 'Data24', 'Data25', 'Data26', 'Data27', 'Data28', 'Data29', 'Data30'),
    ('Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10'),
    ('Data41', 'Data42', 'Data43', 'Data44', 'Data45', 'Data46', 'Data47', 'Data48', 'Data49', 'Data50'),
    ('Data51', 'Data52', 'Data53', 'Data54', 'Data55', 'Data56', 'Data57', 'Data58', 'Data59', 'Data60'),
    ('Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10'),
    ('Data71', 'Data72', 'Data73', 'Data74', 'Data75', 'Data76', 'Data77', 'Data78', 'Data79', 'Data80'),
    ('Data81', 'Data82', 'Data83', 'Data84', 'Data85', 'Data86', 'Data87', 'Data88', 'Data89', 'Data90'),
    ('Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10'),
    ('Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10'),
    ('Data11', 'Data12', 'Data13', 'Data14', 'Data15', 'Data16', 'Data17', 'Data18', 'Data19', 'Data20'),
    ('Data21', 'Data22', 'Data23', 'Data24', 'Data25', 'Data26', 'Data27', 'Data28', 'Data29', 'Data30'),
    ('Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10'),
    ('Data41', 'Data42', 'Data43', 'Data44', 'Data45', 'Data46', 'Data47', 'Data48', 'Data49', 'Data50'),
    ('Data51', 'Data52', 'Data53', 'Data54', 'Data55', 'Data56', 'Data57', 'Data58', 'Data59', 'Data60'),
    ('Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10'),
    ('Data51', 'Data52', 'Data53', 'Data54', 'Data55', 'Data56', 'Data57', 'Data58', 'Data59', 'Data60'),
    ('Data51', 'Data52', 'Data53', 'Data54', 'Data55', 'Data56', 'Data57', 'Data58', 'Data59', 'Data60'),
    ('Data71', 'Data72', 'Data73', 'Data74', 'Data75', 'Data76', 'Data77', 'Data78', 'Data79', 'Data80'),
    ('Data81', 'Data82', 'Data83', 'Data84', 'Data85', 'Data86', 'Data87', 'Data88', 'Data89', 'Data90'),
    ('Data91', 'Data92', 'Data93', 'Data94', 'Data95', 'Data96', 'Data97', 'Data98', 'Data99', 'Data100');

select * from ExampleTable;

-- Set a sufficient length for GROUP_CONCAT
SET SESSION group_concat_max_len = 1000000;

-- Store column names (excluding the first column) in a variable
SET @columns = NULL;

SELECT GROUP_CONCAT(column_name) INTO @columns
FROM information_schema.columns
WHERE table_schema = 'test' AND table_name = 'ExampleTable'
AND column_name != 'ID'; -- Exclude the ID column

-- Construct the dynamic SQL query
SET @sql = CONCAT('
    SELECT ID, COUNT(*) AS occurrence
    FROM ExampleTable
    GROUP BY ', @columns, '
    HAVING COUNT(*) > 1
');

-- Prepare and execute the dynamic SQL query
PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

