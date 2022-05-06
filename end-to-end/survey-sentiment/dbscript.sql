/****** Object:  Table [dbo].[assessments]    Script Date: 8/3/2021 10:21:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[assessments](
	[assessment_id] [bigint] IDENTITY(1,1) NOT NULL,
	[target_id] [bigint] NOT NULL,
	[assessment_sentiment] [varchar](100) NOT NULL,
	[assessment_text] [nvarchar](max) NOT NULL,
	[assessment_positive_score] [decimal](4, 3) NOT NULL,
	[assessment_negative_score] [decimal](4, 3) NOT NULL,
	[assessment_is_negated] [bit] NOT NULL,
 CONSTRAINT [PK_assessments] PRIMARY KEY CLUSTERED 
(
	[assessment_id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[documents]    Script Date: 8/3/2021 10:21:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[documents](
	[document_id] [bigint] IDENTITY(1,1) NOT NULL,
	[internal_document_id] [bigint] NOT NULL,
	[document_sentiment] [varchar](100) NOT NULL,
	[document_positive_score] [decimal](4, 3) NOT NULL,
	[document_neutral_score] [decimal](4, 3) NOT NULL,
	[document_negative_score] [decimal](4, 3) NOT NULL,
 CONSTRAINT [PK_documents] PRIMARY KEY CLUSTERED 
(
	[document_id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Restaurant_Reviews]    Script Date: 8/3/2021 10:21:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Restaurant_Reviews](
	[Review] [nvarchar](150) NOT NULL,
	[Liked] [nvarchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sentences]    Script Date: 8/3/2021 10:21:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sentences](
	[sentence_id] [bigint] IDENTITY(1,1) NOT NULL,
	[document_id] [bigint] NOT NULL,
	[sentence_sentiment] [varchar](100) NOT NULL,
	[sentence_text] [nvarchar](max) NOT NULL,
	[sentence_positive_score] [decimal](4, 3) NOT NULL,
	[sentence_neutral_score] [decimal](4, 3) NOT NULL,
	[sentence_negative_score] [decimal](4, 3) NOT NULL,
 CONSTRAINT [PK_sentences] PRIMARY KEY CLUSTERED 
(
	[sentence_id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[targets]    Script Date: 8/3/2021 10:21:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[targets](
	[target_id] [bigint] IDENTITY(1,1) NOT NULL,
	[sentence_id] [bigint] NOT NULL,
	[target_sentiment] [varchar](100) NOT NULL,
	[target_text] [nvarchar](max) NOT NULL,
	[target_positive_score] [decimal](4, 3) NOT NULL,
	[target_negative_score] [decimal](4, 3) NOT NULL,
 CONSTRAINT [PK_targets] PRIMARY KEY CLUSTERED 
(
	[target_id] ASC
)WITH (STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[assessments]  WITH CHECK ADD  CONSTRAINT [FK_assessments_targets] FOREIGN KEY([target_id])
REFERENCES [dbo].[targets] ([target_id])
GO
ALTER TABLE [dbo].[assessments] CHECK CONSTRAINT [FK_assessments_targets]
GO
ALTER TABLE [dbo].[sentences]  WITH CHECK ADD  CONSTRAINT [FK_documents_sentences] FOREIGN KEY([document_id])
REFERENCES [dbo].[documents] ([document_id])
GO
ALTER TABLE [dbo].[sentences] CHECK CONSTRAINT [FK_documents_sentences]
GO
ALTER TABLE [dbo].[targets]  WITH CHECK ADD  CONSTRAINT [FK_targets_sentences] FOREIGN KEY([sentence_id])
REFERENCES [dbo].[sentences] ([sentence_id])
GO
ALTER TABLE [dbo].[targets] CHECK CONSTRAINT [FK_targets_sentences]
GO
/****** Object:  StoredProcedure [dbo].[InsertAssessment]    Script Date: 8/3/2021 10:21:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE  PROCEDURE [dbo].[InsertAssessment]
(
	@target_id bigint,
	@sentiment varchar(100),
	@assessment_text varchar(max),
	@positive_score decimal(4,3),
	@negative_score decimal(4,3),
	@is_negated bit
)
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO assessments VALUES(@target_id, @sentiment, @assessment_text, @positive_score, @negative_score, @is_negated)
END
GO
/****** Object:  StoredProcedure [dbo].[InsertDocument]    Script Date: 8/3/2021 10:21:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertDocument]
(
	@document_id bigint,
	@sentiment varchar(100),
	@positive_score decimal(4,3),
	@neutral_score decimal(4,3),
	@negative_score decimal(4,3)
)
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO documents VALUES(@document_id, @sentiment, @positive_score, @neutral_score, @negative_score)
    SELECT @@IDENTITY
END
GO
/****** Object:  StoredProcedure [dbo].[InsertSentence]    Script Date: 8/3/2021 10:21:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertSentence]
(
	@document_id bigint,
	@sentiment varchar(100),
	@sentence_text nvarchar(max),
	@positive_score decimal(4,3),
	@neutral_score decimal(4,3),
	@negative_score decimal(4,3)
)
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO sentences VALUES(@document_id, @sentiment, @sentence_text, @positive_score, @neutral_score, @negative_score)
    SELECT @@IDENTITY
END
GO
/****** Object:  StoredProcedure [dbo].[InsertTarget]    Script Date: 8/3/2021 10:21:23 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE PROCEDURE [dbo].[InsertTarget]
(
	@sentence_id bigint,
	@sentiment varchar(100),
	@target_text nvarchar(max),
	@positive_score decimal(4,3),
	@negative_score decimal(4,3)
)
AS
BEGIN
    SET NOCOUNT ON

	INSERT INTO targets VALUES(@sentence_id, @sentiment, @target_text, @positive_score, @negative_score)
    SELECT @@IDENTITY
END
GO
